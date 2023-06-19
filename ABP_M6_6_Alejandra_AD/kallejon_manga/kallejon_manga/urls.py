"""
URL configuration for kallejon_manga project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from kallejon_manga_app.views import lista_usuario,HomeView,MaintenanceView,ProductsView,StoresView,DeliveryView,SignupView,SignupEmployView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/',lista_usuario,name='usuarios'),
    path('', HomeView.as_view(), name='Home'),
    path('mantenimiento/',MaintenanceView.as_view(), name='mantenimiento'),
    path('productos/',ProductsView.as_view(), name='productos'),
    path('tiendas/',StoresView.as_view(), name='tiendas'),
    path('despacho/',DeliveryView.as_view(), name='envios'),
    path('registro/',SignupView.as_view(), name='registro'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('empleados/',SignupEmployView.as_view(), name='empleados'),
]
