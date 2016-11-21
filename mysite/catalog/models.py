from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	Pid = models.CharField(max_length=200);
	Pname = models.CharField(max_length=200);
	Ppicture = models.CharField(max_length=200);
	Pbrand = models.CharField(max_length=200);
	Ptype = models.CharField(max_length=200);
	Pprice = models.FloatField();
	Pamount = models.FloatField();
	Pdetail = models.CharField(max_length=200);

	class Meta:
		app_label = "Product"
		db_table = "product";
