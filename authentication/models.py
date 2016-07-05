from django.db import models
from decimal import Decimal

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
	firstname = models.CharField(max_length=45)
	surename = models.CharField(max_length=45)
	fathername = models.CharField(max_length=45)
	password = models.CharField(max_length=45)
	phone = models.CharField(max_length=14)
	email = models.EmailField(max_length=60)
	city = models.CharField(max_length=30)
	street = models.CharField(max_length=45)
	house_number = models.CharField(max_length=10)
	hash_code = models.CharField(max_length=45)
	datecreate = models.DateField(auto_now=True, auto_now_add=False)

