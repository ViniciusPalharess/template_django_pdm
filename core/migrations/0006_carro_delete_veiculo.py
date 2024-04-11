# Generated by Django 5.0.2 on 2024-04-09 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_veiculo"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carro",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("modelo", models.CharField(max_length=100)),
                ("acessorios", models.ManyToManyField(related_name="carros", to="core.acessorio")),
                (
                    "imagem",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="uploader.image",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Veiculo",
        ),
    ]