from django.db import models

from apps.customer.models import Customer


class Item(models.Model):
	product_name= models.CharField(max_length=20)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	def __str__ (self):
		return '{}'.format(self.product_name)



class Order(models.Model):
	created_at = models.DateField(auto_now=False, auto_now_add=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	product = models.ManyToManyField(Item)
	
	def __str__(self):
		return '{} {}'.format('order from', self.customer)

	