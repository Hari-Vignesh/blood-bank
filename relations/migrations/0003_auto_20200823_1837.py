# Generated by Django 3.0.5 on 2020-08-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0002_auto_20200823_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
