# Generated by Django 5.1 on 2024-08-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Instructor",
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
                ("name", models.CharField(max_length=100)),
                ("bio", models.TextField()),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="instructors/"),
                ),
            ],
        ),
    ]
