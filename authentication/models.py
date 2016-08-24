import datetime

from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User, UserManager

# Create your models here.
class CustomerRestoredPassword(models.Model):
	email = models.EmailField(max_length=60)
	create_date = models.DateField(auto_now=True, auto_now_add=False,)
	key = models.CharField(max_length=20)
	def __str__(self):
		return self.key
	def was_asked(self):
		return self.create_date
class Customer(models.Model):
	user = models.OneToOneField(User)
	fathername = models.CharField(max_length=45)
	phone = models.CharField(max_length=14)
	city = models.CharField(max_length=30)
	street = models.CharField(max_length=45)
	house_number = models.CharField(max_length=10)
	hash_code = models.CharField(max_length=45)
	objects = UserManager()
	activation_key = models.CharField(max_length=40, blank=True)
	key_expires = models.DateTimeField()
	def __str__(self):
		return self.user.username
	def __unicode__(self):
		return self.user
	class Meta:
		verbose_name = 'Профіль'
		verbose_name_plural = 'Профілі'

