
# Create your models here.
from django.db import models
import os

class SharedFile(models.Model):
    name = models.CharField(max_length=255)
    original_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='sent/')
    password = models.CharField(max_length=128, blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    is_received = models.BooleanField(default=False)

    def __str__(self):
        return self.name