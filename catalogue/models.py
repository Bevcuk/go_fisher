from django.db import models

class BigCategory(models.Model):
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=45)
	big_category = models.ForeignKey(BigCategory, default=1)
	def __str__(self):
		return self.name

class Subcategory(models.Model):
	name = models.CharField(max_length=45)
	def __str__(self):
		return self.name