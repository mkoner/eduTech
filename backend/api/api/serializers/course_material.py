from rest_framework import serializers

from ..models.course_material import CourseMaterial

class CourseMaterialSerializer(serializers.ModelSerializer):
    """Serializer for course_material model"""

    class Meta:
        model = CourseMaterial
        fields = '__all__'