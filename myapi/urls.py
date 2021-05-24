from os import name
from django.db import router
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from .views import urlViewset

routers = routers.DefaultRouter()
routers.register(r'youtubeurls', urlViewset)

urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

