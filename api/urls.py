from django.urls import path
from . import views
#Set urls here

app_name = "api"
urlpatterns = [
    path('', views.ArticlesList.as_view(), name="api_view"),
    path('<int:pk>', views.ArticlesDetail.as_view(), name="detail_api_view"),
    path('users/', views.UserList.as_view(), name="list_view_user"),
    path('users/<int:pk>', views.UserDetail.as_view(), name="detail_view_user"),
    path('users/<int:pk>/create', views.UserDetailCreate.as_view(), name="detail_create_view_user"),
]