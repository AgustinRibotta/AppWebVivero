from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PlantasModels

# Create your views here.


class PlantasListView(ListView):
    template_name = "inicio.html"
    context_object_name = 'list'
    
    def get_queryset(self):
        kword = self.request.GET.get('kword')
        
        if not kword:
            planta = PlantasModels.objects.all()
            print(planta )
            return planta
        
        else:

            planta = PlantasModels.objects.filter(
            name = kword.capitalize()
            )
            
            return planta
            

class PlantaDetailView(DetailView):
    model = PlantasModels
    template_name = "info.html"

        



