from django.db import models


class Professionals(models.Model):
    
    social_name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
   
    def __str__(self):
        return self.social_name

