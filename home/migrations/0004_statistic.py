# Generated by Django 5.1 on 2024-09-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_testimonial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Statistic",
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
                ("title", models.CharField(max_length=100)),
                ("value", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=255)),
            ],
        ),
    ]