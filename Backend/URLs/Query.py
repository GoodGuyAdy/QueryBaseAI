from django.urls import path
from Backend.Views.Query import QueryClass

urlpatterns = [
    path("query", QueryClass.as_view()),
]
