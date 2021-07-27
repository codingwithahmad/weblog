from django.contrib import admin
from .models import Articles, Category
# Register your models here.

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'jpublish', 'category_to_str')
    search_fields = ('title', 'author')
    list_filter = ('title', 'publish', 'author')

    def category_to_str(self, obj):
        return ", ".join([ category.title for category in obj.category_publish()])
    category_to_str.short_description = "دسته یندی ها"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    search_fields = ('title', 'slug')
    list_filter = (['status'])