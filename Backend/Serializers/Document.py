from rest_framework import serializers
from Core.DatabaseInjestion.Check import check_doucment, check_org


class DocumentUploadSerializer(serializers.Serializer):
    """This contains serializers to upload a document"""

    file_id = serializers.IntegerField(allow_null=False)
    file = serializers.FileField(allow_null=False)
    org = serializers.CharField(allow_null=False)

    def validate(self, data):
        file_id = data["file_id"]
        org = data["org"]

        org_exists = check_org(org)

        if not org_exists:
            raise serializers.ValidationError("This Organisation does not exists.")

        doc_exists = check_doucment(file_id, org)

        if doc_exists:
            raise serializers.ValidationError("Document with this ID already exists.")

        return data


class DocumentDeleteSerializer(serializers.Serializer):
    """This contains serializers to delete a document"""

    file_id = serializers.IntegerField(allow_null=False)
    org = serializers.CharField(allow_null=False)

    def validate(self, data):
        file_id = data["file_id"]
        org = data["org"]

        org_exists = check_org(org)

        if not org_exists:
            raise serializers.ValidationError("This Organisation does not exists.")

        doc_exists = check_doucment(file_id, org)

        if not doc_exists:
            raise serializers.ValidationError(
                "Document you are trying to delete does not exists."
            )

        return data
