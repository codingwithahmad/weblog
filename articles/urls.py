from django.urls import path, include
from . import views
#Set urls for /articles here
urlpatterns = [
    path('', views.home, name="home"),
]