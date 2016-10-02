from django.db import models
from decimal import Decimal
from catalogue.models import Subcategory, Category
import json
import re
import unidecode

class ProductFrom(models.Model):
	subcategory_id = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
	category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
	def __str__(self):
		return u'%s: %s - %s' % (self.category_id, self.subcategory_id, self.subcategory_id.extra_parameters)

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
	image = models.FileField(upload_to = 'go_fisher/static/go_fisher/img/products', blank=False, null=True)
	def __str__(self):
		return self.name
	def slice_ref(self):
		ref = str(self.image)
		i = ref.find('img/')
		return ref[i:len(ref)]

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
	image = models.FileField(upload_to = 'go_fisher/static/go_fisher/img/brands', blank=False, null=True)
	def __str__(self):
		return self.name
	def slice_ref(self):
		ref = str(self.image)
		i = ref.find('img/')
		return ref[i:len(ref)]

class Product(models.Model):
	LENGTH = 'см'
	WEIGHT = 'гр'
	QUANTITY = 'шт'
	TYPE_OF_MEASUREMENTS = (
		(LENGTH, 'довжина'),
		(WEIGHT, 'вага'),
		(QUANTITY, 'кількість'),
		)
	title = models.CharField(max_length=50)
	description = models.TextField(null=True)
	image = models.ManyToManyField(Image, related_name='images')
	brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
	model = models.CharField(max_length=50, null=True, blank=True)
	from_id = models.ForeignKey(ProductFrom, on_delete=models.PROTECT)
	kind = models.ManyToManyField(Kind)
	special = models.ManyToManyField(Special, null=True)
	price = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
	old_price = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
	create_at = models.DateField(auto_now=True, auto_now_add=False)
	quantity = models.PositiveSmallIntegerField()
	garanty = models.PositiveSmallIntegerField()
	priority = models.IntegerField(blank=True, null=True)
	is_best_offer = models.BooleanField()
	is_active = models.BooleanField()
	is_new = models.BooleanField()
	# value_mesure = models.PositiveSmallIntegerField()
	# measurer = models.CharField(max_length=2,
	# 						choices=TYPE_OF_MEASUREMENTS,
	# 						default=WEIGHT)
	extra_parameters_json = models.TextField(null=True)
	slug_params_json = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.title
	# for creating sluged json-like field
	def save(self):
		extra_dict = json.loads(self.extra_parameters_json)
		slug_extra_list = []
		for key, value in extra_dict.items():
			uni_key = unidecode.unidecode(key).lower()
			sluged_key = re.sub(r'\W+', '-', uni_key)

			uni_value = unidecode.unidecode(value).lower()
			sluged_value = re.sub(r'\W+', '-', uni_value)

			slug_extra_list.append(sluged_key + '=' + sluged_value)
		self.slug_params_json = slug_extra_list
		super(Product, self).save()

	def extra_to_dict(self):
		py_dict = json.loads(self.extra_parameters_json)
		return py_dict

    #
	# def mesurer_name(self):
	# 	if self.measurer == 'см':
	# 		return 'Довжина'
	# 	elif self.measurer == 'гр':
	# 		return 'Вага'
	# 	elif self.measurer == 'шт':
	# 		return 'Кількість'

# clothe models
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
