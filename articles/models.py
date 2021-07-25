from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
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

    class Meta:
        verbose_name="مقاله"
        verbose_name_plural="مقالات"

    def __str__(self):
        return self.title
        