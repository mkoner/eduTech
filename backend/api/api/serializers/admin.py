from rest_framework import serializers
from ..models.admin import Admin

class AdminSerializer(serializers.ModelSerializer):
    """Serializer for Admin model"""
    class Meta:
        model = Admin
        fields = '__all__'

class AdminUpdateSerializer(AdminSerializer):
    """Serializer for updating an existing Learner"""
    class Meta:
        model = Admin
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AdminUpdateSerializer, self).__init__(*args, **kwargs)
        # Make fields optional when updating
        for field_name, field in self.fields.items():
            field.required = False