from accounts.models import User

from rest_framework import serializers



class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializes data for User Registration
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['token']


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user    


class LoginSerializer(serializers.ModelSerializer):
    """
    Serializes data for Login Purposes
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'profile', 'password', 'uuid', 'token')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['token']
