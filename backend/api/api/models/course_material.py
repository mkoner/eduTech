from django.db import models
from .base_model import BaseModel
from .course import Course

class CourseMaterial(BaseModel):
    """Class for the course model"""
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    link = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_materials')