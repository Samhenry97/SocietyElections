from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	major = models.CharField(max_length=50)
	rank = models.CharField(max_length=10)
	position = models.CharField(max_length=20)