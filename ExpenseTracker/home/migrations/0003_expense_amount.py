# Generated by Django 4.1 on 2023-10-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_profile_expenses"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="amount",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
