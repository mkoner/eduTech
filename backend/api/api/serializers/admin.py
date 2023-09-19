from rest_framework import serializers
from ..models.admin import Admin

class AdminSerializer(serializers.ModelSerializer):
    """Serializer for Admin model"""
    class Meta:
        model = Admin
        fields = '__all__'