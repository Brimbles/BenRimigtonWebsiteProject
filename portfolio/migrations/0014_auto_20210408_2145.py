# Generated by Django 3.1.4 on 2021-04-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='{{MEDIA_URL}}images/'),
        ),
        migrations.DeleteModel(
            name='ProjectImage',
        ),
    ]