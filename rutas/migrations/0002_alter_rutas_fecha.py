# Generated by Django 4.1.2 on 2022-11-25 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rutas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rutas",
            name="fecha",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
