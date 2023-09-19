from django.db import models
from .base_model import BaseModel

class Course(BaseModel):
    """Class for the course model"""
    course_name = models.CharField(max_length=250)
    description = models.TextField(default='')