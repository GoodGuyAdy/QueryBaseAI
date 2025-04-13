from rest_framework import serializers
from Core.DatabaseInjestion.Check import check_doucment


class QueryPostSerializer(serializers.Serializer):
    """This contains serializers to post a query"""

    query = serializers.CharField(allow_null=False)
    file_id = serializers.IntegerField(allow_null=True)
    org = serializers.CharField(allow_null=False)

    def validate(self, data):
        file_id = data["file_id"]

        if file_id:
            org = data["org"]
            exists = check_doucment(file_id, org)

            if not exists:
                raise serializers.ValidationError(
                    "Document with this ID does not exists."
                )

        return data
