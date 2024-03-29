from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class PlantasModels(models.Model):
    """Model definition for Plantas."""

    # TODO: Define fields here
    name = models.CharField(
        'Nombre', 
        max_length=30, 
        unique=True
    )
    front = models.ImageField(
        'Imagen de Portada de la Planta', 
        upload_to= 'clase',
    )
    desciption = RichTextField(
        blank=True
    )
    stock = models.BooleanField(default=True)
       
     
    class Meta:
        """Meta definition for Plantas."""

        verbose_name = 'Cargar categoria de Planta'
        verbose_name_plural = 'Categorias de Plantas'

    def __str__(self):

        return self.name 


class PlantaModel(models.Model):
    """Model definition for Planta."""

    # TODO: Define fields here
    name = models.CharField(
        'Nombre', 
        max_length=30, 
        unique=True
    )
    list = models.ImageField(
        'Imagen de la Planta que queres cargar', 
        upload_to='plantas', 
    )
    price = models.DecimalField(
        'Precio', 
        max_digits=5, 
        decimal_places=2, 
        null=0
    )  
    plantas = models.ForeignKey(
        PlantasModels, 
        on_delete=models.CASCADE
    )
    stock = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Planta."""

        verbose_name = 'Cargar una nueva Planta'
        verbose_name_plural = 'Cargar nuevas  Plantas'

    def __str__(self):
        """Unicode representation of Planta."""
        return self.name
