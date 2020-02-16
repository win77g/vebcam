# Generated by Django 2.2.10 on 2020-02-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiveCameras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('name', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('url', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('slug', models.SlugField(blank=True, default=None, null=True)),
                ('top', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]