# Generated by Django 3.2.8 on 2022-09-07 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quitance', '0021_quitance_journee'),
    ]

    operations = [
        migrations.AddField(
            model_name='quitance',
            name='sent_cgib',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
