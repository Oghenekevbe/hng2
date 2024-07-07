from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'firstName', 'lastName', 'email', 'phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'userId': {'read_only': True}
        }

    def validate_email(self, value):
        # Check if email is already in use
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def validate_firstName(self, value):
        # Ensure firstName is not null or empty
        if not value:
            raise serializers.ValidationError("First name cannot be empty.")
        return value

    def validate_lastName(self, value):
        # Ensure lastName is not null or empty
        if not value:
            raise serializers.ValidationError("Last name cannot be empty.")
        return value

    def validate_password(self, value):
        # Ensure password is not null or empty
        if not value:
            raise serializers.ValidationError("Password cannot be empty.")
        return value




class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_email(self, value):
        # Check if email is already in use
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value


    def validate_password(self, value):
        # Ensure password is not null or empty
        if not value:
            raise serializers.ValidationError("Password cannot be empty.")
        return value


