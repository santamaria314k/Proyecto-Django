# Generated by Django 4.2.5 on 2023-09-26 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rol',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id_user', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=20)),
                ('telefono2', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.rol')),
            ],
        ),
    ]
