from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):
	house=models.CharField(max_length=20,default='A-101')
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100, default="society-member")

	def __str__(self):
		return self.fname + "-" + self.lname + "-" + self.usertype

class Events(models.Model):
	date=models.DateTimeField()
	event=models.TextField()

class Notice(models.Model):
	date=models.DateTimeField()
	event=models.TextField()

class Visitor(models.Model):
	name=models.CharField(max_length=100)
	house=models.CharField(max_length=50)
	mobile=models.PositiveIntegerField()
	purpose=models.TextField()
	date=models.DateTimeField()
	vehical=models.CharField(max_length=30,default=True)

	def __str__(self):
		return self.name

class Watchman(models.Model):
	name=models.CharField(max_length=100)
	house=models.ForeignKey(User,on_delete=models.CASCADE)
	mobile=models.PositiveIntegerField()
	complain=models.TextField()
	date=models.DateTimeField()
	status=models.CharField(max_length=100,default='Pending')

	def __str__(self):
		return self.name+'-'+self.house

class Chairman(models.Model):
	maintainance=models.PositiveIntegerField()

class Transaction(models.Model):
	date=models.DateTimeField()
	amount=models.ForeignKey(Chairman,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	payment_status=models.BooleanField(default=False)


	def __str__(self):
		return self.house