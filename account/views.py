from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from articles.models import Articles
from django.views.generic.list import ListView

# Create your views here.
class ArticlesList(LoginRequiredMixin, ListView):
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Articles.objects.all()
        else:
            return Articles.objects.filter(author=self.request.user)
