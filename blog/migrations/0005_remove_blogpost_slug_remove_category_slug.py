# Generated by Django 5.1 on 2024-09-01 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_category_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpost",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="category",
            name="slug",
        ),
    ]
