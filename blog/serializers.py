
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


# class PostSerializer (serializers.ModelSerializer):

#     class Meta :
#         model = Post
#         fields = '__all__'


class AuthorSerializer (serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ['username']


class PostSerializer (serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta :
        model = Post
        fields = '__all__'