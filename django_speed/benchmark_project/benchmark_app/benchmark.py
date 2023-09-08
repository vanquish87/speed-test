# benchmark_project/benchmark.py

import cProfile
from django.contrib.auth.models import User
from benchmark_app.serializers import serialize_user


# Create a user
u = User.objects.create_user(
    username="hakib",
    first_name="haki",
    last_name="benita",
    email="me@hakibenita.com",
)

# Run the benchmark
cProfile.run("for i in range(5000): serialize_user(u)", sort="tottime")
