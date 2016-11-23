from __future__ import unicode_literals

from django.db import models
from catalog.models import *

# Create your models here.
class CartItem(models.Model):
	username = models.CharField(max_length=45)
	Pid = models.CharField(max_length=200)
	Pamount = models.FloatField()
