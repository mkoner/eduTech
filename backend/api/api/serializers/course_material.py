from rest_framework import serializers

from ..models.course_material import CourseMaterial

class CourseMaterialSerializer(serializers.ModelSerializer):
    """Serializer for course_material model"""

    class Meta:
        model = CourseMaterial
        fields = '__all__'


class CourseMaterialUpdateSerializer(CourseMaterialSerializer):
    """Serializer for updating an existing Course material"""
    class Meta:
        model = CourseMaterial
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CourseMaterialUpdateSerializer, self).__init__(*args, **kwargs)
        # Make fields optional when updating
        for field_name, field in self.fields.items():
            field.required = False