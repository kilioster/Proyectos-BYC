from django.urls import path
from . import views

app_name = 'casas'

urlpatterns = [
    path('', views.propiedades, name="list"),
]