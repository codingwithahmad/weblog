from django.contrib.auth import views
from django.urls import path
from .views import (
    ArticlesList,
    ArticlesCreate,
    ArticlesUpdate,
    ArticlesDelete,
    Profile,
    Login,
    
)

app_name = "account"

urlpatterns = [
    path('', ArticlesList.as_view(), name="home"),
    path("article/create", ArticlesCreate.as_view(), name="article-create"),
    path("article/update/<int:pk>", ArticlesUpdate.as_view(), name="article-update"),
    path("article/delete/<int:pk>", ArticlesDelete.as_view(), name="article-delete"),
    path("profile/", Profile.as_view(), name="profile"),
]