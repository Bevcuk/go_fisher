from django.db import models

class BigCategory(models.Model):
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=45)
	big_category = models.ManyToManyField(BigCategory)
	def __str__(self):
		return self.name

class Subcategory(models.Model):
	name = models.CharField(max_length=45)
	def __str__(self):
		return self.name

class SubcategoryBelong(models.Model):
	bigcategory_id = models.ForeignKey(BigCategory, on_delete=models.PROTECT)
	subcategory_id = models.ForeignKey(Category, on_delete=models.PROTECT)
	def __str__(self):
		return u'%s : %s' % (self.bigcategory_id, self.сategory_id)