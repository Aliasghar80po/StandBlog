# Generated by Django 4.2.1 on 2023-08-03 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_alter_profile_image"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="national_code",),
    ]