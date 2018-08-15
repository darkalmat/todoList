from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}        
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')
    
    def create(self, validated_data):
        user = User(
            email = validated_data.get('email', ''),
            first_name = validated_data.get('first_name', ''),
            last_name = validated_data.get('last_name', ''),
            username = validated_data.get('username')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=100)

    class Meta:
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
        }        
        fields = ('email', 'username', 'first_name', 'last_name')
    
    def update(self, user, validated_data):
        user.username = validated_data.get('username', user.username)
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.email = validated_data.get('email', user.email)
        user.save()
        return user
