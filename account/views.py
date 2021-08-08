from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from articles.models import Articles
from django.views.generic.list import ListView

# Create your views here.
class ArticlesList(LoginRequiredMixin, ListView):
    queryset = Articles.objects.all()
    template_name = "registration/home.html"
