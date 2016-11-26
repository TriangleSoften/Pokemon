from __future__ import unicode_literals

from django.db import models

# Create your models here.
class OrderItem(models.Model):
	username = models.CharField(max_length=45)
	Pid = models.CharField(max_length=200)
	Pamount = models.FloatField()
	Orderid = model.IntegerField()

class Order(models.Model):
	username = models.CharField(max_length=45)
	Orderid = model.IntegerField()
	OrderStatus = model.CharField(max_length=45)