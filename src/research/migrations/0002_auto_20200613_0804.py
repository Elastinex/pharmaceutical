# Generated by Django 3.0.7 on 2020-06-13 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='created_on',
            field=models.DateField(max_length=255, verbose_name='Creadted by'),
        ),
    ]
