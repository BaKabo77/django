# Generated by Django 5.2.3 on 2025-06-18 00:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_exo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='date_creation',
        ),
        migrations.AddField(
            model_name='produit',
            name='date_peremption',
            field=models.DateField(default=datetime.datetime(2025, 6, 18, 2, 28, 0, 830592)),
            preserve_default=False,
        ),
    ]
