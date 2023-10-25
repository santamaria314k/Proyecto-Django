# Generated by Django 4.2.5 on 2023-10-15 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposGarantia',
            fields=[
                ('id_tiga', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Garantias',
            fields=[
                ('id_gar', models.AutoField(primary_key=True, serialize=False)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('id_serveh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehiculo.serviciosxvehiculos')),
                ('id_tiga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Garantias.tiposgarantia')),
            ],
        ),
    ]
