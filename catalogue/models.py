from django.db import models
from decimal import Decimal
# Create your models here.
class Size(models.Model):
	size_name = models.CharField(max_length=10)

class BrandClothe(models.Model):
	brand_name = models.SlugField(max_length=40)

class Clothe(models.Model):
	title = models.SlugField(max_length=60)
	description = models.TextField()
	active = models.BooleanField()
	size = models.ForeignKey(Size, on_delete=models.PROTECT)
	brand = models.ForeignKey(BrandClothe, on_delete=models.PROTECT)
	image = models.FileField(upload_to = 'go_fisher/static/shop/images/clothes', blank=False, null=True)

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

class ProductFrom(models.Model):
	subcategory_id = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
	category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
	def __str__(self):
		return u'%s: %s' % (self.category_id, self.subcategory_id)

class Image(models.Model):
	JPEG = 'JPEG'
	PNG = 'PNG'
	IMAGE_EXTENSION = (
		(JPEG, 'jpeg'),
		(PNG, 'png'),
		)
	name = models.CharField(max_length=60)
	extension = models.CharField(max_length=4,
							choices=IMAGE_EXTENSION,
							default=JPEG)
	image = models.FileField(upload_to = 'go_fisher/static/shop/images/products', blank=False, null=True)
	def __str__(self):
		return self.name

class Special(models.Model):
	title = models.CharField(max_length=50)
	priority = models.IntegerField(blank=True, null=True)
	start_at = models.DateField()
	end_at = models.DateField()

class Kind(models.Model):
	name = models.CharField(max_length=45)
	priority = models.IntegerField(blank=True, null=True)
	def __str__(self):
		return self.name

class Brand(models.Model):
	name = models.CharField(max_length=60)
	priority = models.IntegerField(blank=True, null=True)
	image = models.FileField(upload_to = 'go_fisher/static/shop/images/brands', blank=False, null=True)
	def __str__(self):
		return self.name

