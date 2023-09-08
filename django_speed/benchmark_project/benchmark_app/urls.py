# benchmark_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("run_benchmark/", views.run_benchmark, name="run_benchmark"),
]
