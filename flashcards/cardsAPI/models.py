from django.db import models


class Deck(models.Model):
	name = models.CharField(max_length=400, blank=True)
	
class Card(models.Model):
	front = models.CharField(max_length=400, blank=True)
	back = models.CharField(max_length=400, blank=True)
	deck = models.ForeignKey(Deck)

class Document(models.Model):
	description = models.CharField(max_length=255, blank=True)
	document = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	