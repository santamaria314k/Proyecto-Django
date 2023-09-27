from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.db import connection

# @login_required
# def admin(request):
#     return render(request, 'Login/Admin.html')

# @login_required
# def user(request):
#     return render(request, 'Login/User.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Ejecutar una consulta SQL para obtener los datos del usuario
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_rol_id FROM login_usuario WHERE username = %s AND password = %s", [username, password])
                row = cursor.fetchone()

                if row:
                    id_rol_id = row[0]
                    if id_rol_id == 1:
                        return render(request, 'admin.html')
                    elif id_rol_id == 2:
                        return render(request, 'user.html')
                else:
                    messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor, ingresa credenciales válidas.')
    else:
        form = LoginForm()
    
    return render(request, 'registration/Login.html', {'form': form})
