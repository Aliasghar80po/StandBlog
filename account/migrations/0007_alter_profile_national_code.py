# Generated by Django 4.2.1 on 2023-08-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0006_alter_profile_national_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="national_code",
            field=models.IntegerField(default=123456789),
            preserve_default=False,
        ),
    ]
