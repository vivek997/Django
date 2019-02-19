from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import User
from rest_framework.serializers import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'dob', 'email', 'phone_no')
