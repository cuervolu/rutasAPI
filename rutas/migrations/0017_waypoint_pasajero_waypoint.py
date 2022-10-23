# Generated by Django 4.1.2 on 2022-10-23 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rutas", "0016_remove_destino_ruta_remove_origen_ruta_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Waypoint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("latitud", models.FloatField()),
                ("longitud", models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name="pasajero",
            name="waypoint",
            field=models.ManyToManyField(blank=True, to="rutas.waypoint"),
        ),
    ]
