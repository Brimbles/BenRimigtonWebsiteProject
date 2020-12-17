# Generated by Django 3.0.6 on 2020-09-06 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]