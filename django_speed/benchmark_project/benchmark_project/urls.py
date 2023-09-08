# benchmark_project/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("benchmark/", include("benchmark_app.urls")),  # Include your app's URLs here
]
