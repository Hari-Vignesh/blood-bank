# Generated by Django 3.0.5 on 2020-08-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='height',
            field=models.DecimalField(decimal_places=2, default=150, max_digits=5),
        ),
        migrations.AddField(
            model_name='person',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=50, max_digits=5),
        ),
    ]
