from django.shortcuts import render
from .forms import SelectForm # Importamos el Formulario Creado

# Create your views here.

# def selectOption(request):
    # select_form = SelectForm()
    # return render(request, 'selectOption/selectOption.html', {'form ': select_form})


def selectOption(request):
    select_form = SelectForm() # Inicializar el Formulario 
    
    if request.method == 'POST':
        select_form = SelectForm(data=request.POST)
    
    return render(request, 'selectOption/selectOption.html', {'form': select_form}) #Agregamos diccionario de contexto



