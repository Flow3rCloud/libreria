# Generated by Django 4.0.6 on 2022-07-12 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='fecha_publicacion',
        ),
    ]
