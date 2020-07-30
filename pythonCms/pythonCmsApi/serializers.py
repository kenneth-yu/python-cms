from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserModel, Component, Page, Website


class ComponentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'pageId']

class PageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'path', 'websiteId']

class WebsiteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ['id', 'ownerId']

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['url', 'username', 'email', 'testing']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']