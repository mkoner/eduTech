from rest_framework import serializers
from ..models.admin import Admin
from django.contrib.auth.hashers import make_password

class AdminSerializer(serializers.ModelSerializer):
    """Serializer for Admin model"""
    class Meta:
        model = Admin
        fields = '__all__'
    
    def create(self, validated_data):
        ''' Hashes a password before saving in the database '''
        password = make_password(validated_data['password'])
        validated_data['password'] = password
        return Admin.objects.create(**validated_data)

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