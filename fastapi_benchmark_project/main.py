# main.py

from fastapi import FastAPI

# Define your routes and functions here
# Import necessary modules and models
from typing import Dict, Any
from pydantic import BaseModel
from fastapi import HTTPException
import time


# Define a Pydantic model for user data
class UserModel(BaseModel):
    id: int
    last_login: str
    is_superuser: bool
    username: str
    first_name: str
    last_name: str
    email: str
    is_staff: bool
    is_active: bool
    date_joined: str


app = FastAPI()


# Define UserReadOnlyModel similar to DRF serializer
class UserReadOnlyModel(BaseModel):
    id: int
    last_login: str
    is_superuser: bool
    username: str
    first_name: str
    last_name: str
    email: str
    is_staff: bool
    is_active: bool
    date_joined: str


# Define UserSerializer similar to DRF serializer
class UserSerializer(BaseModel):
    id: int
    last_login: str
    is_superuser: bool
    username: str
    first_name: str
    last_name: str
    email: str
    is_staff: bool
    is_active: bool
    date_joined: str


# Define User similar to Django User model
class User(BaseModel):
    id: int
    last_login: str
    is_superuser: bool
    username: str
    first_name: str
    last_name: str
    email: str
    is_staff: bool
    is_active: bool
    date_joined: str


# Create a FastAPI route to benchmark user serialization using UserModelSerializer
@app.get("/benchmark_user_model_serializer/")
async def benchmark_user_model_serializer():
    # Check if the user already exists
    existing_user = get_existing_user()
    if existing_user:
        delete_existing_user(existing_user)

    # Create a user
    u = create_user()

    # Measure the time it takes to serialize using UserModelSerializer
    start_time = time.perf_counter()
    for i in range(5000):
        serialized_data = UserModel(**u.dict())
    end_time = time.perf_counter()

    # Calculate execution time in milliseconds rounded to one decimal place
    execution_time_ms = round((end_time - start_time) * 1000, 1)

    return {
        "execution_time_ms": f"{execution_time_ms} ms",
        "data": serialized_data.dict(),
    }


# Create a FastAPI route to benchmark user serialization using UserReadOnlyModelSerializer
@app.get("/benchmark_user_read_only_model_serializer/")
async def benchmark_user_read_only_model_serializer():
    # Check if the user already exists
    existing_user = get_existing_user()
    if existing_user:
        delete_existing_user(existing_user)

    # Create a user
    u = create_user()

    # Measure the time it takes to serialize using UserReadOnlyModelSerializer
    start_time = time.perf_counter()
    for i in range(5000):
        serialized_data = UserReadOnlyModel(**u.dict())
    end_time = time.perf_counter()

    # Calculate execution time in milliseconds rounded to one decimal place
    execution_time_ms = round((end_time - start_time) * 1000, 1)

    return {
        "execution_time_ms": f"{execution_time_ms} ms",
        "data": serialized_data.dict(),
    }


# Create a FastAPI route to benchmark user serialization using UserSerializer
@app.get("/benchmark_user_serializer/")
async def benchmark_user_serializer():
    # Check if the user already exists
    existing_user = get_existing_user()
    if existing_user:
        delete_existing_user(existing_user)

    # Create a user
    u = create_user()

    # Measure the time it takes to serialize using UserSerializer
    start_time = time.perf_counter()
    for i in range(5000):
        serialized_data = UserSerializer(**u.dict())
    end_time = time.perf_counter()

    # Calculate execution time in milliseconds rounded to one decimal place
    execution_time_ms = round((end_time - start_time) * 1000, 1)

    return {
        "execution_time_ms": f"{execution_time_ms} ms",
        "data": serialized_data.dict(),
    }


# Helper functions
def get_existing_user():
    return UserModel(
        id=1,
        last_login="2023-09-08T12:34:56",
        is_superuser=False,
        username="hakib",
        first_name="haki",
        last_name="benita",
        email="me@hakibenita.com",
        is_staff=False,
        is_active=True,
        date_joined="2023-09-08T12:34:56",
    )


def delete_existing_user(user):
    pass


def create_user():
    return UserModel(
        id=1,
        last_login="2023-09-08T12:34:56",
        is_superuser=False,
        username="hakib",
        first_name="haki",
        last_name="benita",
        email="me@hakibenita.com",
        is_staff=False,
        is_active=True,
        date_joined="2023-09-08T12:34:56",
    )
