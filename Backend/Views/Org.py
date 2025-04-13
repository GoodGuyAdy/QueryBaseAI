from rest_framework.views import APIView
from rest_framework.response import Response
from Backend.Serializers.Org import (
    RegisterOrganisationSerializer,
    DeleteOrganisationSerializer,
)
from Core.DatabaseInjestion.Upload import create_organisation
from Core.DatabaseInjestion.Delete import delete_organisation
from Backend.Serializers.Error.FlatError import serializer_errors


class OrganisationClass(APIView):
    """
    Organisation Post and Delete Class
    """

    def post(self, request):
        """
        Organisation Post Method
        """

        data = {
            "org_name": request.data.get("org_name"),
        }
        serializer = RegisterOrganisationSerializer(data=data)

        if serializer.is_valid():
            org_name = serializer.validated_data["org_name"]
            create_organisation(org_name)
            return Response(
                status=200,
                data={"Message": "Organisation Registered Successfully!"},
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )

    def delete(self, request):
        """
        Organisation Delete Method
        """

        data = {
            "org_name": request.GET.get("org_name"),
        }
        serializer = DeleteOrganisationSerializer(data=data)

        if serializer.is_valid():
            org_name = serializer.validated_data["org_name"]
            delete_organisation(org_name)
            return Response(
                status=200,
                data={"Message": "Organisation Deleted Successfully!"},
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )
