# Generated by Django 2.2 on 2020-07-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20200706_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
