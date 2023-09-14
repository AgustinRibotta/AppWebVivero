from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PlantaModel, PlantasModels

# Create your views here.


class PlantasListView(ListView):
    template_name = "inicio.html"
    context_object_name = 'list'
    
    def get_queryset(self):
        kword = self.request.GET.get('kword','')
        planta = PlantasModels.objects.filter(
        name__icontains= kword.capitalize(),
        stock=True
        ) 
          
        return planta
            

class PlantaDetailView(DetailView):
    model = PlantasModels
    template_name = "info.html"
    
    
    def get_context_data(self, **kwargs):
        context = super(PlantaDetailView, self).get_context_data(**kwargs)
        context['plantas'] = PlantaModel.objects.filter(
            stock=True,
            plantas = context['object']
            )
        return context
        

    
    

        



