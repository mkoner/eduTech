"""Module for encoding and decoding jwt token for authentication"""
import jwt
import datetime
from rest_framework.response import Response
from rest_framework import status

from ..models.admin import Admin
from ..models.learner import Learner

secret = "secret7*&é"
algorithm = "HS256"

def generate_token(user):
    """Generate a token for a particular user after login"""

    
    payload = {
        "user_id": user.id,
        "user_email": user.email,
        "user_type": "admin" if isinstance(user, Admin) else "learner",
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7),
        "iss": "eduTech",
        "iat": datetime.datetime.now(datetime.timezone.utc),
    }

    token = jwt.encode(payload, secret, algorithm)
    return token

def get_user_from_request(request):
    """Retrieves a user from a token"""

    token = request.headers.get("Authorization")
    if token and token.startswith("Token "):
        token = token.split(' ', 1)[1]
        try:
            payload = jwt.decode(token, secret, algorithm, issuer="eduTech")
        except Exception:
            return None
        user_id = payload.get("user_id")
        user_type = payload.get("user_type")
        user = Admin.objects.get(pk=user_id) if user_type == "admin" else Learner.objects.get(pk=user_id)
        return user
    return None

def validate_token(request):
    """Check if a token is passed within resquest and if it starts with Token"""

    token = request.headers.get("Authorization")
    if token and token.startswith("Token "):
        return True
    else:
        return False
    