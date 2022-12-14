# Generated by Django 3.2.8 on 2022-07-20 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quitance', '0011_auto_20220720_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=100, verbose_name='Libele')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='bordereaudetail',
            name='nature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quitance.nature'),
        ),
    ]
