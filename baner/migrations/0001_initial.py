# Generated by Django 2.2.10 on 2020-02-06 21:27

import baner.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=baner.models.image_folder)),
                ('slug', models.SlugField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Банер',
                'verbose_name_plural': 'Банер',
            },
        ),
    ]