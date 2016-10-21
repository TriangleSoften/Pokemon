from __future__ import unicode_literals

from django.db import models

# Create your models here.
class logUsers(models.Model):
	username = models.CharField(max_length=45)
	password = models.CharField(max_length=45)

	class Meta:
		db_table = "userdata"
		app_label = 'Users'