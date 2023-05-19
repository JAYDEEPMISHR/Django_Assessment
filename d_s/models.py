from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100, default="society-member")

	def __str__(self):
		return self.fname + "-" + self.lname

class Events(models.Model):
	date=models.DateTimeField()
	event=models.TextField()

class Notice(models.Model):
	date=models.DateTimeField()
	event=models.TextField()

	