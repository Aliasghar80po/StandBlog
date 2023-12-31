# Generated by Django 4.2.4 on 2023-08-11 08:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_article_author_alter_article_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(help_text='enter your description', verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='images/articles', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=True, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_column='mytitle', help_text='Choose your title', max_length=50, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
    ]
