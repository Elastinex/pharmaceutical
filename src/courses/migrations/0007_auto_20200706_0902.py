# Generated by Django 2.2 on 2020-07-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20200706_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='image_field',
            field=models.ImageField(default='default', upload_to='kurs_images', verbose_name='Зураг оруулах'),
        ),
    ]
