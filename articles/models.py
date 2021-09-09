from django.db import models
from django.urls import reverse
from django.utils import timezone
from myweblog import settings
from extends.jtime import jalali_convertor
from django.utils.html import format_html
from account.models import User
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

class ArticlesManager(models.Manager):
    def published(self):
        return self.filter(status="p")
    

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)
# Create your models here.
class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس آی پی")

    class Meta:
        verbose_name = "نشانی آی پی"
        verbose_name_plural = "نشانی های آی پی"

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="children", verbose_name="زیردسته", null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس")
    status = models.BooleanField(default=True, verbose_name="آیا نشان داده شود؟")
    position = models.IntegerField(verbose_name="جایگاه")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    objects = CategoryManager()



class Articles(models.Model):
    STATUS_CHOICES = [
        ('p', 'منتشرشده'),
        ('d', 'پیش نویس'),
        ('i', 'در حال بررسی'),
        ('b', 'برگشت داده شده'),
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
    is_special = models.BooleanField(default=False, verbose_name="مقاله ویژه")
    category = models.ManyToManyField(Category, verbose_name="دسته یندی", related_name="articles")
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress, through="ArticleHit", related_name="hits", blank=True, verbose_name="بازدید ها")

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

    def category_to_str(self):
        return ", ".join([ category.title for category in self.category_publish()])
    category_to_str.short_description = "دسته یندی ها"

    def get_absolute_url(self):
        return reverse("account:home")

class ArticleHit(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)