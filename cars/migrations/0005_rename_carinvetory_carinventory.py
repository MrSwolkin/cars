# Generated by Django 5.1.1 on 2024-09-26 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0004_carinvetory"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CarInvetory",
            new_name="CarInventory",
        ),
    ]
