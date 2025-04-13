import json
import logging
from django.utils.deprecation import MiddlewareMixin
from QueryBaseAI.settings import LOG_ALL_REQUESTS

api_logger = logging.getLogger("api_logger")

APP_JSON = "application/json"
MULTIPART_FORM = "multipart/form-data"
CONTENT_TYPE = "Content-Type"
TRACEBACK_KEY = "traceback"
BINARY_CONTENT_TYPES = {
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/octet-stream",
}


class LogstashLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        is_multipart = MULTIPART_FORM in request.content_type
        request.body_data = None if is_multipart else request.body
        request.res_traceback_data = None

    def process_response(self, request, response):
        """
        Logs request and response data based on LOG_ALL_REQUESTS setting.

        Logs all requests if enabled, or only responses with status >= 400.
        Handles and strips traceback data from 500 responses if present.
        """
        response_status_code = response.status_code
        if not LOG_ALL_REQUESTS and response_status_code < 400:
            return response

        if (
            response_status_code == 500
            and getattr(response, "headers", {}).get(CONTENT_TYPE) == APP_JSON
        ):
            try:
                response_data = json.loads(response.content)
            except json.JSONDecodeError:
                response_data = None

            if response_data and TRACEBACK_KEY in response_data:
                request.res_traceback_data = {
                    "res_exception": response_data.get("msg"),
                    "res_traceback": response_data.get(TRACEBACK_KEY),
                }
                del response_data[TRACEBACK_KEY]
                response.content = json.dumps(response_data)

        request_headers = dict(request.headers)
        response_headers = dict(response.items())
        request_path = request.path
        request_method = request.method

        request_content_type = request_headers.get(CONTENT_TYPE, "")
        response_content_type = response_headers.get(CONTENT_TYPE, "")

        if MULTIPART_FORM in request_content_type:
            request_data = request.POST.copy()
            if request.FILES:
                request_data["files"] = "Uploaded Files"
            request_body = json.dumps(request_data)
        else:
            request_body = (
                request.body_data.decode("utf-8") if request.body_data else ""
            )

        if response_content_type in BINARY_CONTENT_TYPES:
            response_text = "A File"
        else:
            response_text = response.content.decode("utf-8") if response.content else ""

        log_data = {
            "req_headers": request_headers,
            "req_path": request_path,
            "req_body": request_body,
            "res_status_code": response_status_code,
            "res_text": response_text,
            "res_headers": response_headers,
            "req_method": request_method,
        }

        if request.res_traceback_data:
            log_data.update(
                {
                    "res_exception": request.res_traceback_data.get("res_exception"),
                    "res_traceback": request.res_traceback_data.get("res_traceback"),
                }
            )

        try:
            api_logger.info(
                f"{request_method} {request_path} Request Log", extra=log_data
            )
        except Exception as e:
            api_logger.error(f"Failed to log request/response data: {str(e)}")

        return response
