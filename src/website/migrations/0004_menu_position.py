# Generated by Django 3.0.7 on 2020-07-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200723_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='position',
            field=models.IntegerField(default='0', verbose_name='Menu position'),
        ),
    ]
