from django.shortcuts import render
from django.views.generic import ListView
from .models import PlantasModels

# Create your views here.


class PlantasListView(ListView):
    model = PlantasModels
    template_name = "inicio.html"
    context_object_name = 'list'
    


