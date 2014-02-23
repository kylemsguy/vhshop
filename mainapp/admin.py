from django.contrib import admin
from mainapp.models import Company, DimsGlasses, Glasses

# Register your models here.

class GlassesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company Name', {'fields': ['company',]}),
        ('Dimensions', {'fields': ['dimensions']}),
        ('User Related', {'fields': ['numtries', 'likes', \
                                     'numtries_to_likes']}),
    ]

class CompanyAdmin(admin.ModelAdmin):
    fields = ['CompName', 'website']

class DimsGlassesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['GlassesName']}),
        ('Left Side', {'fields': ['left_side_x', 'left_side_y']}),
        ('Right Side', {'fields': ['right_side_x', 'right_side_y']}),
        ('Sides (General)', {'fields': ['sides', 'widthsides']}),
        ('Left Bridge', {'fields': ['left_bridge_x', 'left_bridge_y']}),
        ('Right Bridge', {'fields': ['right_bridge_x', 'right_bridge_y']}),
        ('Bridges (General)', {'fields': ['bridge', 'widthbridges']}),
    ]

admin.site.register(Glasses)
admin.site.register(Company)
admin.site.register(DimsGlasses)
