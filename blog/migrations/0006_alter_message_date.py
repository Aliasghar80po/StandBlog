# Generated by Django 4.2.4 on 2023-08-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
