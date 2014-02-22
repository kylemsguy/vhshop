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
    left_side = (self.left_side_x, self.left_side_y)
    
    right_side_x = models.IntegerField()
    right_side_y = models.IntegerField()
    right_side = (self.right_side_x, self.right_side_y)
    
    sides = [self.left_side, self.right_side]

    def width(self):
        return sqrt(\
                ((abs(self.right_side_x - self.left_side_x))**2) + \
                ((abs(self.right_side_y - self.left_side_y))**2))

    # Eyes
    left_eye_x = models.IntegerField()
    left_eye_y = models.IntegerField()
    left_eye = (self.left_eye_x, self.left_eye_y)
    
    right_eye_x = models.IntegerField()
    right_eye_y = models.IntegerField()
    right_eye = (self.right_eye_x, self.right_eye_y)
    
    eyes = [self.left_eye, self.right_eye]

    def __str__(self):
        return [self.sides, self.eyes]

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
    
