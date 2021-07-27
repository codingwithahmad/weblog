from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from extends.jtime import jalali_convertor


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس")
    status = models.BooleanField(default=True, verbose_name="آیا نشان داده شود؟")
    position = models.IntegerField(verbose_name="جایگاه")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "ذسته بندی ها"
        ordering = ['position']

    def __str__(self):
        return self.title




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

    def __str__(self):
        return self.title
        