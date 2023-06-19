from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def lista_usuario(request) -> HttpResponse:
    from django.contrib.auth.models import User
    users = User.objects.all()
    return render(request, 'kallejon_manga_app/usuarios.html', {'users': users})

class HomeView(TemplateView):
    template_name = 'kallejon_manga_app/home.html'

class MaintenanceView(TemplateView):
    template_name = 'kallejon_manga_app/mantenimiento.html'

class ProductsView(TemplateView):
    template_name = 'kallejon_manga_app/mantenimiento.html'

class StoresView(TemplateView):
    template_name = 'kallejon_manga_app/mantenimiento.html'

class DeliveryView(TemplateView):
    template_name = 'kallejon_manga_app/mantenimiento.html'