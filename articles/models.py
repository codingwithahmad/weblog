from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from extends.jtime import jalali_convertor
from django.utils.html import format_html

# Create your models here.
class ArticlesManager(models.Manager):
    def published(self):
        return self.filter(status="p")
    

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)



class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="children", verbose_name="زیردسته", null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس")
    status = models.BooleanField(default=True, verbose_name="آیا نشان داده شود؟")
    position = models.IntegerField(verbose_name="جایگاه")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "ذسته بندی ها"
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    objects = CategoryManager()



class Articles(models.Model):
    STATUS_CHOICES = [
        ('p', 'منتشرشده'),
        ('d', 'پیش نویس')
    ]

    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    description = models.TextField(verbose_name="متن")
    thumbnail = models.ImageField(upload_to="Images", null=True, verbose_name="تصویر")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    create = models.DateTimeField(auto_now_add=True, verbose_name="زمان نوشتار")
    update = models.DateTimeField(auto_now=True, verbose_name="زمان بروزرسانی")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="وضعیت")
    category = models.ManyToManyField(Category, verbose_name="دسته یندی", related_name="articles")

    class Meta:
        verbose_name="مقاله"
        verbose_name_plural="مقالات"

    def jpublish(self):
        return jalali_convertor(self.publish)
    jpublish.short_description = "زمان انتشار"

    def category_publish(self):
        return self.category.filter(status=True)

    objects = ArticlesManager()

    def __str__(self):
        return self.title
        
    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}' >".format(self.thumbnail.url))

    thumbnail_tag.short_description = "عکس"