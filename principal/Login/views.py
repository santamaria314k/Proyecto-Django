from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import Usuario

#Fucines de acceso para el login
def admin(request):
    return render(request,'Admin.html')

def user(request):
    return render(request,'User.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_rol_id FROM login_usuario WHERE username = %s AND password = %s", [username, password])
                row = cursor.fetchone()
                
           
            if row :
                id_rol_id = row[0]
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



