from django.db import models
from decimal import Decimal
from product.models import Product
from authentication.models import Customer
# Create your models here.
class Delivery(models.Model):
	NP = '1'
	UP = '2'
	DIF = '3'
	TYPE_OF_DELIVERY = (
		(NP, 'Нова пошта'),
		(UP, 'Укрпошта'),
		(DIF, 'Інший вид доставки'),
		)
	delivery_name = models.CharField(max_length=20,
										choices=TYPE_OF_DELIVERY)
	priority = models.IntegerField(blank=True, null=True)

class OrderStatus(models.Model):
	OPERATED = '1'
	SENDED = '2'
	DELIVERED = '3'
	COMPLETE = '4'
	STEP_IN_OPERATING = (
		(OPERATED, 'Operated'),
		(SENDED, 'Sended'),
		(DELIVERED, 'Delivered'),
		(COMPLETE, 'Complete'),
		)
	status = models.CharField(max_length=10,
								choices=STEP_IN_OPERATING,
								default=OPERATED)
	priority = models.IntegerField(blank=True, null=True)

# should be rewrited too
class Payment(models.Model):
	payment = models.CharField(max_length=25)
	priority = models.IntegerField(blank=True, null=True)

class Order(models.Model):
	create_at = models.DateField(auto_now=True, auto_now_add=False)
	product = models.ManyToManyField(Product)
	total_price = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
	comment = models.CharField(max_length=255)
	delivery_id = models.ForeignKey(Delivery, on_delete=models.PROTECT)
	customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
	status_id = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
	payment_id = models.ForeignKey(Payment, on_delete=models.PROTECT)
