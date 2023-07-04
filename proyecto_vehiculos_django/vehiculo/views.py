from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo
from .forms import RegistroUsuarioForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Permission, User


# Create your views here.
def index(request):
    return render(request, 'index.html')

# se usara para verificar los permisos de los usuarios
def has_permission(user):
    return user.has_perms(['vehiculo.visualizar_catalogo', 'vehiculo.add_vehiculomodel'])

# Ingresar un vehiculo
@login_required
@user_passes_test(has_permission)
def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save()
            messages.info(request, "Vehiculo ingresado satisfactoriamente")
            return redirect('listar')
    else:
        form = VehiculoForm()
    
    return render(request, 'vehiculo_form.html', {'form': form})


# Listar todos los vehiculos
@login_required 
@user_passes_test(has_permission)
def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'listar.html', {'vehiculos': vehiculos})

# Registro de Usuarios
def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            # Crear un nuevo usuario con is_staff=True (para que pueda acceder al panel administrativo)
            user = User.objects.create_user(username=username, password=password1, is_staff=True)
            
            login(request, user)
            messages.success(request, "Registrado satisfactoriamente.")

            # Asignar permisos al usuario nuevo
            visualizar_catalogo_permission = Permission.objects.get(codename='visualizar_catalogo')
            add_vehiculomodel_permission = Permission.objects.get(codename='add_vehiculomodel')
            add_vehiculo_permission = Permission.objects.get(codename='add_vehiculo')
            view_vehiculo_permission = Permission.objects.get(codename='view_vehiculo')
            admin_permission = Permission.objects.get(codename='access_admin')
            user.user_permissions.add(visualizar_catalogo_permission, add_vehiculomodel_permission, admin_permission, add_vehiculo_permission, view_vehiculo_permission)

            return HttpResponseRedirect('/')
        messages.error(request, "Registro inválido. Algunos datos ingresados no son correctos.")

    form = RegistroUsuarioForm()
    return render(request=request, template_name="registro.html", context={"register_form": form})

# Login de Usuarios
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesion como {username}")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Usuario o Contraseña invalida")
        else:
            messages.error(request, "Usuario o Contraseña invalida")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={'login_form': form})

# Cerrar sesion
def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la session satisfactoriamente")
    return HttpResponseRedirect("/")