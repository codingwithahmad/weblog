from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
	email = models.EmailField(unique=True, verbose_name="ایمیل")

	is_author = models.BooleanField(default=False, verbose_name="وضعیت نویسندگی")
	special_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")

	def is_special(self):
		if self.special_user > timezone.now():
			return True
		else:
			return False
	
	is_special.boolean = True 
	is_special.short_description = "وضعیت کاربر ویژه"			