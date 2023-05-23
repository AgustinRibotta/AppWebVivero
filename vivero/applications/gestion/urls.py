from django.urls import path
from .views import PlantasListView

urlpatterns = [

    path('list', PlantasListView.as_view(), name='Planta'),

]
