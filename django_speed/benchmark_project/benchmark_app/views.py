# benchmark_app/views.py

import time
from django.contrib.auth.models import User
from django.http import HttpResponse

# Import the serialize_user function from the serializers module
from .serializers import serialize_user, UserModelSerializer, UserReadOnlyModelSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


def run_benchmark(request):
    # Check if the user already exists
    existing_user = User.objects.filter(username="hakib").first()

    if existing_user:
        existing_user.delete()

    # Create a user
    u = User.objects.create_user(
        username="hakib",
        first_name="haki",
        last_name="benita",
        email="me@hakibenita.com",
    )

    # Measure the time it takes to run the benchmark
    start_time = time.perf_counter()
    for i in range(5000):
        serialize_user(u)
    end_time = time.perf_counter()

    # Calculate execution time in milliseconds rounded to one decimal place
    execution_time_ms = round((end_time - start_time) * 1000, 1)

    return HttpResponse(f"Benchmark completed in {execution_time_ms} ms.")


@api_view(["GET"])
def benchmark_user_model_serializer(request):
    # Check if the user already exists
    existing_user = User.objects.filter(username="hakib").first()

    if existing_user:
        existing_user.delete()

    # Create a user
    u = User.objects.create_user(
        username="hakib",
        first_name="haki",
        last_name="benita",
        email="me@hakibenita.com",
    )

    # Measure the time it takes to serialize using UserModelSerializer
    start_time = time.perf_counter()
    for i in range(5000):
        serialized_data = UserModelSerializer(u).data
    end_time = time.perf_counter()

    # Calculate execution time in milliseconds rounded to one decimal place
    execution_time_ms = round((end_time - start_time) * 1000, 1)

    return Response({"execution_time_ms": f"{execution_time_ms} ms", "data": serialized_data})


@api_view(["GET"])
def benchmark_user_read_only_model_serializer(request):
    # Check if the user already exists
    existing_user = User.objects.filter(username="hakib").first()

    if existing_user:
        existing_user.delete()

    # Create a user
    u = User.objects.create_user(
        username="hakib",
        first_name="haki",
        last_name="benita",
        email="me@hakibenita.com",
    )

    # Measure the time it takes to serialize using UserReadOnlyModelSerializer
    start_time = time.perf_counter()
    for i in range(5000):
        serialized_data = UserReadOnlyModelSerializer(u).data
    end_time = time.perf_counter()

    # Calculate execution time in milliseconds rounded to one decimal place
    execution_time_ms = round((end_time - start_time) * 1000, 1)

    return Response({"execution_time_ms": f"{execution_time_ms} ms", "data": serialized_data})


@api_view(["GET"])
def benchmark_user_serializer(request):
    # Check if the user already exists
    existing_user = User.objects.filter(username="hakib").first()

    if existing_user:
        existing_user.delete()

    # Create a user
    u = User.objects.create_user(
        username="hakib",
        first_name="haki",
        last_name="benita",
        email="me@hakibenita.com",
    )

    # Measure the time it takes to serialize using UserReadOnlyModelSerializer
    start_time = time.perf_counter()
    for i in range(5000):
        serialized_data = UserSerializer(u).data
    end_time = time.perf_counter()

    # Calculate execution time in milliseconds rounded to one decimal place
    execution_time_ms = round((end_time - start_time) * 1000, 1)

    return Response({"execution_time_ms": f"{execution_time_ms} ms", "data": serialized_data})
