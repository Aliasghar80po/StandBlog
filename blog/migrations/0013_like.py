# Generated by Django 4.2.4 on 2023-08-12 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_alter_article_created_alter_category_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked', to='blog.article', verbose_name='مقاله')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'لابک',
                'verbose_name_plural': 'لایک ها',
                'ordering': ('created_at',),
            },
        ),
    ]
