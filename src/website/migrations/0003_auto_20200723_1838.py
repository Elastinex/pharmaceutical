# Generated by Django 3.0.7 on 2020-07-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200723_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='is_special',
            field=models.BooleanField(default=False, verbose_name='boxed'),
        ),
    ]
