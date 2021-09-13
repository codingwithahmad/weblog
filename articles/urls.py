from django.urls import path, include
from . import views
#Set urls for /articles here
app_name = "articles"
urlpatterns = [
    path("", views.ArticlesList.as_view(), name="home"),
    path("page/<int:page>", views.ArticlesList.as_view(), name="home"),
    path('details/<slug:slug>', views.ArticleDetail.as_view(), name="details"),
    path('preview/<int:pk>', views.ArticlePreview.as_view(), name="preview"),
    path('category/<slug:slug>', views.category_articles, name="category"),
    path('search/', views.SearchList.as_view(), name="search"),
    path('search/page/<int:page>', views.SearchList.as_view(), name="search"),
]