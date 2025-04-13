from django.urls import path
from Backend.Views.Org import OrganisationClass

urlpatterns = [
    path("organisation", OrganisationClass.as_view()),
]
