from django.db import models

# Create your models here.

options =[
    [0, 'Genero'],
    [1, 'Nacionalidad'], 
    [2, 'Estado Civil'],
    [3, 'Deporte Preferido'],
    [4, 'Tipo de Música'],
    [5, 'Tipo de Comida'],
    [6, 'Tipo de Bebida'],
    [7, 'Tipo de Contacto'] 
]

class SelectOption(models.Model):
    contact_type = models.IntegerField(choices=options, verbose_name='Criterio de Selección')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Envío') 

