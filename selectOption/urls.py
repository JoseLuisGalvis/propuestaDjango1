from django.urls import path
from .views import selectOption

urlpatterns = [
    path('', selectOption, name='selectOption'),
]