# Generated by Django 4.1 on 2023-10-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile", name="expenses", field=models.FloatField(null=True),
        ),
    ]
