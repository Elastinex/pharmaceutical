# Generated by Django 3.0.7 on 2020-10-21 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_auto_20201021_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='alt_text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Carousel image alt text'),
        ),
    ]
