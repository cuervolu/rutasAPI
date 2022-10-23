# Generated by Django 4.1.2 on 2022-10-22 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rutas", "0010_remove_destino_ruta_remove_origen_ruta_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rutas",
            name="destino",
        ),
        migrations.RemoveField(
            model_name="rutas",
            name="origen",
        ),
        migrations.RemoveField(
            model_name="rutas",
            name="pasajero",
        ),
        migrations.AddField(
            model_name="destino",
            name="ruta",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ruta_destino",
                to="rutas.rutas",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="origen",
            name="ruta",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ruta_origen",
                to="rutas.rutas",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pasajero",
            name="ruta",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ruta_pasajero",
                to="rutas.rutas",
            ),
            preserve_default=False,
        ),
    ]
