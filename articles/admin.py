from django.contrib import admin
from .models import Articles, Category
from django.contrib.auth.models import User

# Admin panel template edit

admin.site.site_header = "مدیریت وبلاگ"


# Register your models here.ر
@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'author_full_name', 'status', 'is_special', 'jpublish', 'category_to_str')
    search_fields = ('title', 'author')
    list_filter = ('title', 'publish', 'author')
    actions = ["make_published", "make_draft"]


    def author_full_name(self, obj):
        return obj.author.get_full_name()

    author_full_name.short_description = "نویسنده"
    

    @admin.action(description="منتشر کردن مقالات انتخابی")
    def make_published(self, request, queryset):
        row_updated = queryset.update(status="p")
        if row_updated == 1:
            message_bit = "منتشر شد"
        else:
            message_bit = "منتشر شدند"

        self.message_user(request, "{} مقاله {}".format(row_updated, message_bit))

    @admin.action(description="پیش نویس کردن مقالات انتخابی")
    def make_draft(self, request, queryset):
        row_updated = queryset.update(status="d")
        if row_updated == 1:
            message_bit = "پیش نویس شد"
        else:
            message_bit = "پیش نویس شدند"

        self.message_user(request, "{} مقاله {}".format(row_updated, message_bit))

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    search_fields = ('title', 'slug')
    list_filter = (['status'])
    actions = ["make_action", "make_disable"]

    @admin.action(description="فعال کردن دسته یندی های انتخابی")
    def make_action(self, request, queryset):
        row_updated = queryset.update(status=True)
        if row_updated == 1:
            message_bit = "فعال شد"
        else:
            message_bit = "فعال شدند"
        
        self.message_user(request, "{} دسته بندی {}".format(row_updated, message_bit) )

    @admin.action(description="غیرفعال کردن دسته یندی های انتخابی")
    def make_disable(self, request, queryset):
        row_updated = queryset.update(status=False)
        if row_updated == 1:
            message_bit = "غیرفعال شد"
        else:
            message_bit = "غیرفعال شدند"
        
        self.message_user(request, "{} دسته بندی {}".format(row_updated, message_bit) )
    