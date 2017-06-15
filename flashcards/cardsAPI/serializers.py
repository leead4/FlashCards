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