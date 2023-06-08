from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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

] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

