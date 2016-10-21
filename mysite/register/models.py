from __future__ import unicode_literals

from django.db import models

# Create your models here.
class regUsers(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=45)
	password = models.CharField(max_length=45)
	firstname = models.CharField(max_length=45)
	lastname = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	gender = models.CharField(max_length=45)
	dateofbrith = models.CharField(max_length=45)
	phonenum = models.CharField(max_length=45)

	class Meta:
		db_table = "userdata"
		app_label = 'Users'