from django.db import models
from decimal import Decimal
from catalogue.models import Subcategory, Category
# Create your models here.

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
	image = models.FileField(upload_to = 'go_fisher/static/images/products', blank=False, null=True)
	def __str__(self):
		return self.name

class Special(models.Model):
	title = models.CharField(max_length=50)
	priority = models.IntegerField(blank=True, null=True)
	start_at = models.DateField()
	end_at = models.DateField()
	def __str__(self):
		return u'%s - %s - %s' % (self.title, self.start_at, self.end_at)

class Kind(models.Model):
	name = models.CharField(max_length=45)
	priority = models.IntegerField(blank=True, null=True)
	def __str__(self):
		return self.name

class Brand(models.Model):
	name = models.CharField(max_length=60)
	priority = models.IntegerField(blank=True, null=True)
	image = models.FileField(upload_to = 'go_fisher/static/images/brands', blank=False, null=True)
	def __str__(self):
		return self.name

class Product(models.Model):
	LENGTH = 'm'
	WEIGHT = 'kg'
	QUANTITY = 'p'
	TYPE_OF_MEASUREMENTS = (
		(LENGTH, 'meters'),
		(WEIGHT, 'kilograms'),
		(QUANTITY, 'pieces'),
		)
	title = models.CharField(max_length=50)
	priority = models.IntegerField(blank=True, null=True)
	description = models.TextField()
	kind = models.ManyToManyField(Kind)
	special = models.ManyToManyField(Special)
	image = models.ManyToManyField(Image)
	create_at = models.DateField(auto_now=True, auto_now_add=False)
	price = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
	old_price = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
	quantity = models.PositiveSmallIntegerField()
	garanty = models.PositiveSmallIntegerField()
	is_best_offer = models.BooleanField()
	is_active = models.BooleanField()
	is_new = models.BooleanField()
	value_mesure = models.PositiveSmallIntegerField()
	measurer = models.CharField(max_length=2,
							choices=TYPE_OF_MEASUREMENTS,
							default=WEIGHT)
	brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT)
	from_id = models.ForeignKey(ProductFrom, on_delete=models.PROTECT)
	json = models.TextField()
	def __str__(self):
		return self.title

# close models
class Size(models.Model):
	size_name = models.CharField(max_length=10)
	def __str__(self):
		return self.name

class BrandClothe(models.Model):
	brand_name = models.SlugField(max_length=40)
	def __str__ (self):
		return self.brand_name

class Clothe(models.Model):
	title = models.SlugField(max_length=60)
	description = models.TextField()
	active = models.BooleanField()
	size = models.ForeignKey(Size, on_delete=models.PROTECT)
	brand = models.ForeignKey(BrandClothe, on_delete=models.PROTECT)
	image = models.FileField(upload_to = 'go_fisher/static/images/clothes', blank=False, null=True)
	def __str__(self):
		return self.title
