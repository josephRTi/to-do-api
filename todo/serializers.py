from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Node


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, data):
        print(data)
        if User.objects.filter(email=data).exists():
            raise serializers.ValidationError('Пользователь с данным email уже существует')
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError({'password': 'Пароли должны совпадать'})

        user.set_password(validated_data['password'])
        user.save()
        return user


class NodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ['id', 'user', 'node', 'is_finished', 'date']
