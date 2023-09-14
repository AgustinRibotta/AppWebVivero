from django.contrib import admin
from .models import PlantaModel, PlantasModels

# Register your models here.

class PlantasAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

    
admin.site.register(PlantasModels, PlantasAdmin)


class PlantaAdmin(admin.ModelAdmin):
    '''Admin View for '''
    search_fields = ('name',)
    list_filter  = ('plantas',)

    
admin.site.register(PlantaModel, PlantaAdmin)