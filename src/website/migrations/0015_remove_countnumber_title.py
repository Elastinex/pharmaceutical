# Generated by Django 3.0.7 on 2020-07-24 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20200724_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countnumber',
            name='title',
        ),
    ]
