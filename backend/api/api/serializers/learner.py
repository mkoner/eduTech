from rest_framework import serializers
from ..models.learner import Learner
from django.contrib.auth.hashers import make_password

class LearnerSerializer(serializers.ModelSerializer):
    """Serializer for Learner model"""
    class Meta:
        model = Learner
        fields = '__all__'

    def create(self, validated_data):
        ''' Hashes a password before saving in the database '''
        password = make_password(validated_data['password'])
        validated_data['password'] = password
        return Learner.objects.create(**validated_data)
    
class LearnerUpdateSerializer(LearnerSerializer):
    """Serializer for updating an existing Learner"""
    class Meta:
        model = Learner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LearnerUpdateSerializer, self).__init__(*args, **kwargs)
        # Make fields optional when updating
        for field_name, field in self.fields.items():
            field.required = False