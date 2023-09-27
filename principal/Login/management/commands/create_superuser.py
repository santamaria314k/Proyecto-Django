from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from Login.models import Rol

class Command(BaseCommand):
    help = 'Crea un superusuario personalizado'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        email = 'kevinsantamaria55@gmail.com'
        direccion = 'vtjkg8-9'
        genero = 'Masculino'
        password = '100'

        try:
            rol_superusuario = Rol.objects.get(id=1)
        except Rol.DoesNotExist:
            self.stdout.write(self.style.ERROR('No se encontró un rol con id 1.'))
            return

        try:
            user = User.objects.create_superuser(
                email=email,
                direccion=direccion,
                genero=genero,
                password=password,
                id_rol=rol_superusuario,
            )
            self.stdout.write(self.style.SUCCESS('Superusuario creado correctamente.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al crear el superusuario: {str(e)}'))
