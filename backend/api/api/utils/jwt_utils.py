"""Module for encoding and decoding jwt token for authentication"""
import jwt
import datetime

from ..models.admin import Admin
from ..models.learner import Learner

secret = "secret7*&é"
algorithm = "HS256"

def generate_token(user, type):
    """Generate a token for a particular user after login"""

    payload = {
        "user_id": user.id,
        "user_email": user.email,
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7),
        "iss": "eduTech",
        "aud": type,
        "iat": datetime.datetime.now(datetime.timezone.utc),
    }

    token = jwt.encode(payload, secret, algorithm)
    return token

def get_user_from_token(token, type):
    """Retrieves a user from a token"""

    payload = jwt.decode(token, secret, algorithm, issuer="eduTech", audience=type)
    print(payload)