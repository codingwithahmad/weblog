from django.urls import path
from . import views
#Set urls here

app_name = "api"
urlpatterns = [
    path('', views.ArticlesList.as_view(), name="api_view"),
]