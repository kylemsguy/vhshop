from django.contrib import admin
from mainapp.models import Company, DimsGlasses, Glasses

# Register your models here.

class GlassesAdmin(admin.ModelAdmin):
    list_display = ('company', 'numtries', 'likes', 'numtries_to_likes', \
                    'admin_image')
    fieldsets = [
        ('Company Name', {'fields': ['company',]}),
        ('Dimensions', {'fields': ['dimensions']}),
        ('User Related', {'fields': ['numtries', 'likes']}),
        ('Picture', {'fields': ['picture']}),
    ]

class CompanyAdmin(admin.ModelAdmin):
    fields = ['CompName', 'website']

class DimsGlassesAdmin(admin.ModelAdmin):
    list_display = ('GlassesName', 'widthsides', 'widthbridges')
    fieldsets = [
        ('Name', {'fields': ['GlassesName']}),
        ('Left Side', {'fields': ['left_side_x', 'left_side_y']}),
        ('Right Side', {'fields': ['right_side_x', 'right_side_y']}),
        ('Left Bridge', {'fields': ['left_bridge_x', 'left_bridge_y']}),
        ('Right Bridge', {'fields': ['right_bridge_x', 'right_bridge_y']}),
    ]

admin.site.register(Glasses, GlassesAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(DimsGlasses, DimsGlassesAdmin)
