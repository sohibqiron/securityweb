from django.db import models

# Create your models here.

class Security(models.Model):
    full_name = models.CharField(max_length=70)
    specialty = models.CharField(max_length=55)
    images = models.ImageField(upload_to='security/')
    
    def __str__(self):
        return self.full_name