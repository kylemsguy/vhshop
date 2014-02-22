from django.db import models
from math import sqrt

# Create your models here.

class Company(models.Model):
    CompName = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    
    def __str__(self):
        return self.CompName

class DimsGlasses(models.Model):
    # Sides
    left_side_x = models.IntegerField()
    left_side_y = models.IntegerField()
    left_side = (left_side_x, left_side_y)
    
    right_side_x = models.IntegerField()
    right_side_y = models.IntegerField()
    right_side = (right_side_x, right_side_y)
    
    sides = [left_side, right_side]

    def widthsides(self):
        return sqrt(\
                ((abs(self.right_side_x - self.left_side_x))**2) + \
                ((abs(self.right_side_y - self.left_side_y))**2))

    # Bridges
    left_bridge_x = models.IntegerField()
    left_bridge_y = models.IntegerField()
    left_bridge = (left_bridge_x, left_bridge_y)
    
    right_bridge_x = models.IntegerField()
    right_bridge_y = models.IntegerField()
    right_bridge = (right_bridge_x, right_bridge_y)
    
    bridge = [left_bridge, right_bridge]

    def widthbridges(self):
        return sqrt(\
                ((abs(self.right_bridge_x - self.left_bridge_x))**2) + \
                ((abs(self.right_bridge_y - self.left_bridge_y))**2))

    def __str__(self):
        return [self.sides, self.bridge]

class Glasses(models.Model):
    company = models.ForeignKey(Company)
    dimensions = models.ForeignKey(DimsGlasses)
    GlassesName = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    numtries = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='glasses')

    def numtries_to_likes(self):
        return self.numtries/self.likes

    def __str__(self):
        return self.GlassesName
    
