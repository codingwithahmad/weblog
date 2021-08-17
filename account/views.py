from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from articles.models import Articles
from .mixins import FieldsMixin, FormValid
from django.views.generic import ListView, CreateView

# Create your views here.
class ArticlesList(LoginRequiredMixin, ListView):
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Articles.objects.all()
        else:
            return Articles.objects.filter(author=self.request.user)


class ArticlesCreate(LoginRequiredMixin, FieldsMixin, FormValid, CreateView):
    model = Articles
    fields = ["title", "slug", "author", "description", "thumbnail", "publish", "status", "category",]
    template_name = "registration/articles_create_update.html"