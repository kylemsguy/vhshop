from django.db import models
from math import sqrt
from vhshop.settings import MEDIA_ROOT, STATIC_URL

# Create your models here.

# Glasses Database

class Company(models.Model):
    CompName = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    
    def __str__(self):
        return self.CompName

class DimsGlasses(models.Model):
    GlassesName = models.CharField(max_length=200)
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
        return self.GlassesName

class Glasses(models.Model):
    company = models.ForeignKey(Company)
    dimensions = models.ForeignKey(DimsGlasses)
    likes = models.IntegerField(default=0)
    numtries = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='glasses')

    def admin_image(self):
        print(MEDIA_ROOT)
        return '<img src="%s%s"/>' % (STATIC_URL, self.picture.url)

    admin_image.allow_tags = True

    def numtries_to_likes(self):
        if self.likes == 0:
            return 0
        return self.numtries/self.likes

    def __str__(self):
        return self.dimensions.GlassesName
    

# Face Database

class Face(models.Model):
    image = models.ImageField(upload_to='faces')

    # Sides
    left_side_x = models.IntegerField()
    left_side_y = models.IntegerField()
    left_side = left_side_x, left_side_y
    
    right_side_x = models.IntegerField()
    right_side_y = models.IntegerField()
    right_side = right_side_x, right_side_y
    
    sides = [left_side, right_side]

    def widthsides(self):
        return sqrt(\
                ((abs(self.right_side_x - self.left_side_x))**2) + \
                ((abs(self.right_side_y - self.left_side_y))**2))

    # Eye Corners
    left_corner_x = models.IntegerField()
    left_corner_y = models.IntegerField()
    left_corner = left_corner_x, left_corner_y
    
    right_corner_x = models.IntegerField()
    right_corner_y = models.IntegerField()
    right_corner = right_corner_x, right_corner_y
    
    corner = [left_corner, right_corner]

    def widthcorners(self):
        return sqrt(\
                ((abs(self.right_corner_x - self.left_corner_x))**2) + \
                ((abs(self.right_corner_y - self.left_corner_y))**2))

    def __str__(self):
        return self.id
    
