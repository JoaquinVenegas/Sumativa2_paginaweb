# Generated by Django 5.0.4 on 2024-04-15 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juegos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de juego')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de juego')),
                ('precio', models.IntegerField(verbose_name='Precio de juego')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad de juego')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de usuario')),
                ('username', models.CharField(max_length=60, verbose_name='Nombre de usuario')),
                ('password', models.CharField(max_length=12, verbose_name='Contraseña de usuario')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo de usuario')),
                ('fecha_nac', models.DateField(verbose_name='Fecha de nacimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.usuario', verbose_name='Usuario')),
                ('descripcion', models.CharField(max_length=150, verbose_name='Descripcion de perfil')),
            ],
        ),
    ]
