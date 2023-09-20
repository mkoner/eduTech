from django.db import models
from .base_model import BaseModel

class Admin(BaseModel):
    """ Admin user definition"""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)