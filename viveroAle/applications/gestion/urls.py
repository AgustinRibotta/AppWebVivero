from django.urls import path
from .views import PlantasListView, PlantaDetailView

urlpatterns = [

    path(
        '', 
        PlantasListView.as_view(), 
        name='plantas'
    ),
    path(
        'detai/<pk>/', 
        PlantaDetailView.as_view(), 
        name='planta'
    ),

] 

