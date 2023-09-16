from django.db import models

class Admin(models.Model):
    """ Admin user definition"""
    createdAt = models.DateTimeField()