from django.contrib import admin
from .models import Articles
# Register your models here.

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'jpublish',)
    search_fields = ('title', 'author')
    list_filter = ('title', 'publish', 'author')