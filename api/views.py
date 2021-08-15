#from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from articles.models import Articles
from account.models import User
from .serializer import ArticleSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class ArticlesList(ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


class ArticlesDetail(RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

class UserList(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailCreate(CreateAPIView, RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer