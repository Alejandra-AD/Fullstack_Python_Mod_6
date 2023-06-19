from email.headerregistry import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from kallejon_manga_app.forms import SignupForm, LoginForm, SignupEmployForm

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

class SignupView(TemplateView):
    template_name = 'registration/registro_usuario.html'
    form_class = SignupForm
    success_url = reverse_lazy('Home')

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect | HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})

class LoginView(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Home')
            form.add_error('username', 'Credenciales incorrectas')
            return render(request, self.template_name, {"form": form})
        else:
            return render(request, self.template_name, {"form": form})
        
# class SignupEmployView(TemplateView):
#     template_name = 'registration/registro_empleados.html'
#     form_class = SignupForm
#     success_url = reverse_lazy('Home')

#     def post(self, request, *args, **kwargs) -> HttpResponseRedirect | HttpResponse:
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
#             login(request, user)
#             return redirect(self.success_url)

#         return render(request, self.template_name, {'form': form})

from django.contrib.auth.models import Group

class SignupEmployView(TemplateView):
    template_name = 'registration/registro_empleados.html'
    form_class = SignupEmployForm
    success_url = reverse_lazy('Home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Guarda el usuario sin guardar en la base de datos
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Crea los grupos si no existen
            group1, _ = Group.objects.get_or_create(name='Grupo 1')
            group2, _ = Group.objects.get_or_create(name='Grupo 2')

            group_name = form.cleaned_data['group_choice']
            if group_name == 'grupo1':
                user.groups.add(group1)
            elif group_name == 'grupo2':
                user.groups.add(group2)

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})

