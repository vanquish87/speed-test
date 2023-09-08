# benchmark_app/serializers.py

from typing import Dict, Any
from django.contrib.auth.models import User


def serialize_user(user: User) -> Dict[str, Any]:
    return {
        "id": user.id,
        "last_login": user.last_login.isoformat() if user.last_login is not None else None,
        "is_superuser": user.is_superuser,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "is_staff": user.is_staff,
        "is_active": user.is_active,
        "date_joined": user.date_joined.isoformat(),
    }
