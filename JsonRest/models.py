from django.db import models

# Create your models here.

class JsonData(models.Model):
    data = models.TextField()
    
    
    def __str__(self):
        return self.data