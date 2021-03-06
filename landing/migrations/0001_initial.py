# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 04:59
from __future__ import unicode_literals

from django.db import migrations, models
import landing.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido_paterno', models.CharField(max_length=100, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=100, verbose_name='Apellido Materno')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='asistentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido_paterno', models.CharField(max_length=255)),
                ('apellido_materno', models.CharField(max_length=255)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=255)),
                ('institucion_de_procedencia', models.CharField(max_length=255)),
                ('talleres_disponibles', models.IntegerField(choices=[(3, 'Taller 3'), (2, 'Taller 2'), (1, 'Taller 1')])),
            ],
            options={
                'verbose_name': 'Asistentes',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='ponentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineas_tematicas', models.IntegerField(choices=[(1, 'Análisis teórico (CCAT)'), (2, 'Investigación empírica en educación (CCIE)'), (3, 'Investigación empírica en la salud (CCIS)'), (4, 'Análisis teórico sobre el desarrollo de habilidades para la vida. (HVAT)'), (5, 'Estrategias de enseñanza y desarrollo de habilidades para la vida (IEHVE)'), (6, 'Habilidades socioemocionales (IEHSE)'), (7, 'Habilidades cognoscitivas (IEHC)'), (8, 'Habilidades de investigación en ciencias(IEHIC)'), (9, 'Habilidades de investigación en humanidades (IEHIH)'), (10, 'Evaluación de habilidades para la vida (IEEHV)')])),
                ('titulo', models.CharField(max_length=255)),
                ('a1_nombre', models.CharField(max_length=255)),
                ('a1_apellido_paterno', models.CharField(max_length=255)),
                ('a1_apellido_materno', models.CharField(max_length=255)),
                ('a1_correo_electronico', models.EmailField(max_length=254)),
                ('a1_telefono', models.CharField(max_length=255)),
                ('a1_institucion_de_procedencia', models.CharField(max_length=255)),
                ('a2_nombre', models.CharField(max_length=255)),
                ('a2_apellido_paterno', models.CharField(max_length=255)),
                ('a2_apellido_materno', models.CharField(max_length=255)),
                ('a3_nombre', models.CharField(max_length=255)),
                ('a3_apellido_paterno', models.CharField(max_length=255)),
                ('a3_apellido_materno', models.CharField(max_length=255)),
                ('documento', models.FileField(upload_to=landing.models.content_file_name)),
            ],
            options={
                'verbose_name': 'Ponentes',
                'ordering': ('titulo',),
            },
        ),
    ]
