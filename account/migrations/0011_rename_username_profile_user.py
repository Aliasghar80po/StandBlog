# Generated by Django 4.2.1 on 2023-08-06 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0010_rename_user_profile_username_profile_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile", old_name="username", new_name="user",
        ),
    ]
