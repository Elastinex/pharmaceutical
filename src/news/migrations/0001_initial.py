# Generated by Django 3.0.7 on 2020-06-11 02:59

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Бүлэг',
                'verbose_name_plural': 'Бүлэгүүд',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('author', models.CharField(max_length=255, verbose_name='Author')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content')),
                ('image', models.ImageField(upload_to='media/news/', verbose_name='Image')),
                ('created_on', models.CharField(max_length=255, verbose_name='Creadted by')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Нийтлэл',
                'verbose_name_plural': 'Нийтлэлүүд',
                'ordering': ['created_on'],
            },
        ),
    ]
