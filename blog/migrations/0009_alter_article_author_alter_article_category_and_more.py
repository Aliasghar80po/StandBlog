# Generated by Django 4.2.4 on 2023-08-11 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_alter_comment_options_alter_message_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده مقاله'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name='دسته بندی'),
        ),
    ]