# benchmark_app/views.py

import time
from django.contrib.auth.models import User
from django.http import HttpResponse

# Import the serialize_user function from the serializers module
from .serializers import serialize_user

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
    
    execution_time = end_time - start_time

    return HttpResponse(f"Benchmark completed in {execution_time} seconds.")
