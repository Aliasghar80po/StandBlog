# Generated by Django 4.2.1 on 2023-08-03 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_profile_national_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="national_code",
            field=models.IntegerField(max_length=10),
        ),
    ]
