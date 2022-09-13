# Generated by Django 3.2.8 on 2022-07-21 22:16

from django.db import migrations, models
import quitance.models


class Migration(migrations.Migration):

    dependencies = [
        ('quitance', '0014_auto_20220721_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quitance',
            name='numero',
            field=models.CharField(blank=True, default=quitance.models.get_next_num, max_length=15, null=True, verbose_name='Numero Quittance'),
        ),
        migrations.AlterField(
            model_name='quitance',
            name='numero_dr',
            field=models.CharField(blank=True, default=quitance.models.get_dr_next_num, max_length=100, null=True, verbose_name='Numero Declaration recette'),
        ),
    ]