# Generated by Django 3.2.8 on 2022-08-25 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quitance', '0020_auto_20220825_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='quitance',
            name='journee',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='quitance.journee'),
            preserve_default=False,
        ),
    ]
