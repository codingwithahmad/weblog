from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articles, Category
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from account.mixins import AuthorAccessMixin
from django.db.models import Count, Q
from datetime import datetime, timedelta

#Create your views here

# def home(request, page=1):
#     articles_list = Articles.objects.published()
#     paginator = Paginator(articles_list, 2)
#     articles = paginator.get_page(page)
#     content = {
#         "articles": articles
#     }
#     return render(request, 'articles/articles_list.html', content)

class ArticlesList(ListView):
    model = Articles
    #context_object_name = "articles"
    queryset = Articles.objects.published()
    paginate_by = 2

# def details(request, slug):
#     content = {
#         "article": get_object_or_404(Articles, slug=slug)
#     }
#     return render(request, 'articles/single.html', content)

class ArticleDetail(DetailView):

    context_object_name = "article"

    def get_object(self):
        slug = self.kwargs.get("slug")
        article = get_object_or_404(Articles.objects.published(), slug=slug)

        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)


        return article

class ArticlePreview(AuthorAccessMixin, DetailView):

    context_object_name = "article"

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Articles, pk=pk)


def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug, status=True)
    articles = category.articles.published()
    content = {
        "articles": articles
    }
    return render(request, 'articles/category.html', content)

