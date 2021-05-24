from django.db import models

# Create your models here.
class youtubeURL(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name    