# Generated by Django 3.2.8 on 2022-08-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quitance', '0019_config_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='code',
            field=models.SlugField(max_length=20, unique=True, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='config',
            name='libele',
            field=models.CharField(max_length=100, unique=True, verbose_name='Libele'),
        ),
    ]
