# Generated by Django 2.2.10 on 2020-02-14 19:30

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=news.models.image_folder)),
                ('slug', models.SlugField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, default=None, max_length=200, null=True)),
                ('description_short', models.TextField(blank=True, default=None, max_length=200, null=True)),
                ('author', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('commentari', models.IntegerField(blank=True, default=None, null=True)),
                ('hot_news', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]