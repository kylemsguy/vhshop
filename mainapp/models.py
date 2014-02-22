from django.db import models

# Create your models here.

class Company(models.Model):
    CompName = models.CharField(max_length=200)
    
    def __str__(self):
        return self.CompName

class Glasses(models.Model):
    company = models.ForeignKey(Company)
    GlassesName = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    numtries = models.IntegerField(default=0)
    pictures = models.ImageField(upload_to='glasses')
    def numtries_to_likes(self):
        return self.numtries/self.likes
    def __str__(self):
        return self.GlassesName
    
