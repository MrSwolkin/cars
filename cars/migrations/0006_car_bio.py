# Generated by Django 5.1.1 on 2024-09-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0005_rename_carinvetory_carinventory"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]
