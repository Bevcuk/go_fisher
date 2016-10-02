from django.db import models
import json
import unidecode
from unidecode import unidecode
from django.template.defaultfilters import slugify

class BigCategory(models.Model):
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=45)
	big_category = models.ForeignKey(BigCategory, default=1)
	slug = models.SlugField(default='')
	def __str__(self):
		return self.name

class Subcategory(models.Model):
	name = models.CharField(max_length=45)
	extra_parameters = models.TextField(null=True)
	image = models.FileField(upload_to = 'go_fisher/static/go_fisher/img/subcategories/', blank=False, null=True)
	slug = models.SlugField(default='')
	def __str__(self):
		return self.name
	def slice_ref(self):
		ref = str(self.image)
		i = ref.find('img/')
		return ref[i:len(ref)]
	def extra_to_dict(self):
		py_dict = json.loads(self.extra_parameters)
		return py_dict