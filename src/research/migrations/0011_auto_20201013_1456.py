# Generated by Django 3.0.7 on 2020-10-13 06:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0010_auto_20200803_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='law',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Created on'),
        ),
    ]
