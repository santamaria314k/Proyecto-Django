import pymysql



def user(request):
    return render(request,'pages/User.html')

def admin(request):
    return render(request,'pages/Admin.html')


def verificar_usuario(username, password):
    # Establece la conexión a la base de datos
    connection = pymysql.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        db='mechanics',
        cursorclass=pymysql.cursors.DictCursor 
        )
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM login_usuario WHERE username=%s AND password=%s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            return result 
    finally:
        connection.close()
        
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # User is authenticated, log them in
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                if user.id_rol_id == 1:
                    return redirect('Admin')
                elif user.id_rol_id == 2:
                    return redirect('User')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            print("Form errors:", form.errors)
    else:
        form = LoginForm()

    return render(request, 'pages/Login.html', {'form': form})
