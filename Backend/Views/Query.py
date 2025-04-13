from rest_framework.views import APIView
from rest_framework.response import Response
from Backend.Serializers.Query import QueryPostSerializer
from LLM.Response.Main import get_ai_response
from Backend.Serializers.Error.FlatError import serializer_errors


class QueryClass(APIView):
    """
    Query Class
    """

    def post(self, request):
        """
        Query Upload Method
        """

        data = {
            "query": request.data.get("query"),
            "file_id": request.data.get("file_id"),
            "org": request.headers.get("org"),
        }
        serializer = QueryPostSerializer(data=data)

        if serializer.is_valid():
            query = serializer.validated_data["query"]
            org = serializer.validated_data["org"]
            file_id = serializer.validated_data["file_id"]
            response = get_ai_response(query, org, file_id)
            return Response(
                status=200,
                data={"Response": response},
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )
