import re
from rest_framework import serializers
from Core.DatabaseInjestion.Check import check_org


class RegisterOrganisationSerializer(serializers.Serializer):
    """This contains serializers to upload a document"""

    org_name = serializers.CharField(max_length=50, allow_null=False)

    def validate(self, data):
        org_name = data["org_name"]

        if re.search(r"[^a-z0-9]", org_name):
            raise serializers.ValidationError(
                "Organization name must only contain lowercase letters and numbers."
            )

        exists = check_org(org_name)

        if exists:
            raise serializers.ValidationError(
                "Organization with this name already exists."
            )

        return data


class DeleteOrganisationSerializer(serializers.Serializer):
    """This contains serializers to delete a Organisation"""

    org_name = serializers.CharField(max_length=50, allow_null=False)

    def validate(self, data):
        org_name = data["org_name"]

        exists = check_org(org_name)

        if not exists:
            raise serializers.ValidationError(
                "Organisation you are trying to delete does not exists."
            )

        return data
