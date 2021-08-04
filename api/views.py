#from django.shortcuts import render
from rest_framework.generics import ListAPIView
from articles.models import Articles
from .serializer import ArticleSerializer
# Create your views here.

class ArticlesList(ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer