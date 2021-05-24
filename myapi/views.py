from django.conf.urls import url
from myapi.Serialize import URLSerializer
from os import name
from rest_framework import viewsets
from .models import youtubeURL
import random

class urlViewset(viewsets.ModelViewSet):  
    queryset = youtubeURL.objects.all().order_by('?')[:1]
    serializer_class = URLSerializer