from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import youtubeURL

class URLSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = youtubeURL
		fields = ['id', 'url', 'name']


