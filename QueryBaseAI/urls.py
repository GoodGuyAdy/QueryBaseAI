"""
URL configuration for QueryBaseAI.
"""

from django.contrib import admin
from django.urls import path, include
from Constant.URLs import URLConstants

urlpatterns = [
    path("admin/", admin.site.urls),
    path(URLConstants.url_header, include("Backend.URLs.Org")),
    path(URLConstants.url_header, include("Backend.URLs.Document")),
    path(URLConstants.url_header, include("Backend.URLs.Query")),
]
