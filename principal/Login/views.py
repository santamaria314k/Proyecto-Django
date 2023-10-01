from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from django.db import connection
from .models import Usuario
from django.contrib.auth import logout

#--------------------------------------------


#>>>>>>>>>>>>>>>>>>>>>>--PROTECCION--<<<<<<<<<<<<<<<<<<<<<<

from functools import wraps
from django.contrib import messages

def proteccion_rutas(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.session.get('username') or not request.session.get('password'):
                return redirect('login')

            username = request.session.get('username')
            password = request.session.get('password')

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_rol_id FROM login_usuario WHERE username = %s AND password = %s", [username, password])
                row = cursor.fetchone()

            if row and row[0] in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'No tienes permiso para acceder a esta página.')
                return redirect('login')
        return wrapper
    return decorator


#>>>>>>>>>>>>>>>>>>>>>>--ADMINISTRADOR--<<<<<<<<<<<<<<<<<<<<<<
def admin(request):
    if not request.session.get('username') or not request.session.get('password'):
        return redirect('login')

    username = request.session.get('username')
    password = request.session.get('password')

    
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_rol_id FROM login_usuario WHERE username = %s AND password = %s", [username, password])
        row = cursor.fetchone()

    if row and row[0] == 1:
        return render(request, 'Admin.html')
    else:
        messages.error(request, 'No tienes permiso para acceder a esta página.')
        return redirect('login')

def user(request):
    if not request.session.get('username') or not request.session.get('password'):
        return redirect('login')

    username = request.session.get('username')
    password = request.session.get('password')

    
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_rol_id FROM login_usuario WHERE username = %s AND password = %s", [username, password])
        row = cursor.fetchone()

    if row and row[0] == 2:
        return render(request, 'User.html')
    else:
        messages.error(request, 'No tienes permiso para acceder a esta página.')
        return redirect('login')

#>>>>>>>>>>>>>>>>>>>>>>--LOGIN--<<<<<<<<<<<<<<<<<<<<<<
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_rol_id FROM login_usuario WHERE username = %s AND password = %s", [username, password])
                row = cursor.fetchone()
                
            if row:
                id_rol_id = row[0]
                request.session['username'] = username
                request.session['password'] = password

                if id_rol_id == 1:
                    return redirect('admin')
                elif id_rol_id == 2:
                    return redirect('user')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor, ingresa credenciales válidas.')
    else:
        form = LoginForm()
    
    return render(request, 'registration/Login.html', {'form': form})


#>>>>>>>>>>>>>>>>>>>>>>--CERRAR SESSION--<<<<<<<<<<<<<<<<<<<<<<

def cerrar(request):
    logout(request)
    return redirect('login')
