from rest_framework.views import APIView
from rest_framework.response import Response
from Backend.Serializers.Document import (
    DocumentUploadSerializer,
    DocumentDeleteSerializer,
)
from Core.DatabaseInjestion.Upload import upload_doucment
from Core.DatabaseInjestion.Delete import delete_doucment
from Backend.Serializers.Error.FlatError import serializer_errors


class DocumentClass(APIView):
    """
    Document Upload and Delete Class
    """
    def post(self, request):
        """
        Document Upload Method
        """

        data = {
            "file": request.FILES.get("file"),
            "file_id": request.POST.get("file_id"),
            "org": request.headers.get("org"),
        }
        serializer = DocumentUploadSerializer(data=data)

        if serializer.is_valid():
            file_id = serializer.validated_data["file_id"]
            file = serializer.validated_data["file"]
            org = serializer.validated_data["org"]
            upload_doucment(file_id, file, org)
            return Response(
                status=200,
                data={"Message": "Document Uploaded"},
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )

    def delete(self, request):
        """
        Document Delete Method
        """

        data = {
            "file_id": request.GET.get("file_id"),
            "org": request.headers.get("org"),
        }
        serializer = DocumentDeleteSerializer(data=data)

        if serializer.is_valid():
            file_id = serializer.validated_data["file_id"]
            org = serializer.validated_data["org"]
            delete_doucment(file_id, org)
            return Response(
                status=200,
                data={"Message": "Document Deleted"},
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )
