from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CartItem(models.Model):
	username = models.CharField(max_length=45);
	Pid = models.CharField(max_length=200);
	Pname = models.CharField(max_length=200);
	Ppicture = models.CharField(max_length=200);
	Pprice = models.FloatField();
	Pamount = models.FloatField();
