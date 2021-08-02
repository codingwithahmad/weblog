from django.urls import path, include
from . import views
#Set urls for /articles here
app_name = "articles"
urlpatterns = [
    path('', views.home, name="home"),
    path('page/<int:page>', views.home, name="home"),
    path('details/<slug:slug>', views.ArticleDetail.as_view(), name="details"),
    path('category/<slug:slug>', views.category_articles, name="category")
]