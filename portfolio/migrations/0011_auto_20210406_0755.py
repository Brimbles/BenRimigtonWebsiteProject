# Generated by Django 3.1.4 on 2021-04-06 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20210406_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='images',
            field=models.FileField(upload_to='images/'),
        ),
    ]
