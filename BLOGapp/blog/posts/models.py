from django.db import models
from datetime import datetime
# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now,blank=True)