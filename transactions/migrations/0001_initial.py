# Generated by Django 4.1.3 on 2022-11-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("transaction", models.CharField(max_length=1)),
                ("date", models.CharField(max_length=10)),
                ("value", models.FloatField()),
                ("cpf", models.CharField(max_length=11)),
                ("card", models.CharField(max_length=12)),
                ("hour", models.CharField(max_length=8)),
                ("owner", models.CharField(max_length=14)),
                ("store", models.CharField(max_length=19)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
