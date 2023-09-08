# benchmark_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("run_benchmark/", views.run_benchmark, name="run_benchmark"),
    path(
        "benchmark_user_model_serializer/",
        views.benchmark_user_model_serializer,
        name="benchmark_user_model_serializer",
    ),
    path(
        "benchmark_user_read_only_model_serializer/",
        views.benchmark_user_read_only_model_serializer,
        name="benchmark_user_read_only_model_serializer",
    ),
    path(
        "benchmark_user_serializer/",
        views.benchmark_user_serializer,
        name="benchmark_user_serializer",
    ),
]
