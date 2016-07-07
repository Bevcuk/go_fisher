from django.db import models
from decimal import Decimal
from catalogue.models import Kind, Special, Image, Brand, ProductFrom
# Create your models here.
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
	#image_path_id = models.ForeignKey(Image, on_delete=models.PROTECT)
	from_id = models.ForeignKey(ProductFrom, on_delete=models.PROTECT)
	json = models.TextField()
	def __str__(self):
		return self.title