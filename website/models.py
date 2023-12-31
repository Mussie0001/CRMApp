from django.db import models

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_Name = models.CharField(max_length=50)
	last_Name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=10)
	address =  models.CharField(max_length=75)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_Name} {self.last_Name}")
