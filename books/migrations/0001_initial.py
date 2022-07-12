# Generated by Django 4.0.6 on 2022-07-12 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('portada', models.ImageField(upload_to='portadas/', verbose_name='Portada')),
                ('fecha_publicacion', models.DateField(null=True, verbose_name='Fecha de publicación')),
                ('isbn', models.CharField(max_length=15, null=True, verbose_name='ISBN')),
            ],
        ),
    ]
