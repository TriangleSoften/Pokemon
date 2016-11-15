from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserData(models.Model):
	username = models.CharField(max_length=45)
	gender = models.CharField(max_length=45)
	dateofbirth = models.CharField(max_length=45)
	phonenum = models.CharField(max_length=45)
