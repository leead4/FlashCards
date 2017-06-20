from django.contrib.auth.models import User
from cardsAPI.models import * 
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name')

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Document
		fields = ('description', 'document', 'uploaded_at')

class CardSerializer(serializers.HyperlinkedModelSerializer):
	deck = serializers.CharField(source="deck.name")
	id = serializers.IntegerField(read_only = True)
	class Meta:
		model = Card
		fields = ('id', 'front', 'back', 'deck')

class DeckSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only = True)
	class Meta:

		model = Deck
		fields = ['name', 'id']