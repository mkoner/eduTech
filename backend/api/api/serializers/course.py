from rest_framework import serializers

from ..models.course import Course

class CourseSerializer(serializers.ModelSerializer):
    """Serializer for course model"""
    class Meta:
        model = Course
        fields = '__all__'

class CourseUpdateSerializer(CourseSerializer):
    """Serializer for updating an existing Learner"""
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CourseUpdateSerializer, self).__init__(*args, **kwargs)
        # Make fields optional when updating
        for field_name, field in self.fields.items():
            field.required = False