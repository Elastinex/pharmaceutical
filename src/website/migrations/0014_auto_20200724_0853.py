# Generated by Django 3.0.7 on 2020-07-24 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_presidents_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('number', models.IntegerField(verbose_name='Numbers')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('position', models.IntegerField(default='0')),
            ],
            options={
                'verbose_name': 'Count number',
                'ordering': ['-position'],
            },
        ),
        migrations.AlterModelOptions(
            name='presidents',
            options={'ordering': ['-title'], 'verbose_name': 'Presidents'},
        ),
    ]
