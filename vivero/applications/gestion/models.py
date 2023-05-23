from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class PlantasModels(models.Model):
    """Model definition for Plantas."""

    # TODO: Define fields here
    name = models.CharField('Nombre', max_length=30)
    # front = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    # detail = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    price = models.DecimalField('Precio', max_digits=5, decimal_places=2, null=0)  
    desciption = RichTextField(blank=True)
       
     
    class Meta:
        """Meta definition for Plantas."""

        verbose_name = 'Planta'
        verbose_name_plural = 'Plantas'

    def __str__(self):

        return self.name 