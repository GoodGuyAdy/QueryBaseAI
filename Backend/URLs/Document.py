from django.urls import path
from Backend.Views.Document import DocumentClass

urlpatterns = [
    path("document", DocumentClass.as_view()),
]
