from django.db import models

class User(models.Model):
	name = models.CharField(max_length=25)

	# Create your models here.

	def __str__(self):

		return "{} {}".format(self.name)

class Document(models.Model):
	description = models.CharField(max_length=255, blank=True)
	document = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	