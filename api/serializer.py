from rest_framework import serializers
from articles.models import Articles
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Articles
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'