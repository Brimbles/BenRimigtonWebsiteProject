# Generated by Django 3.1.4 on 2021-04-06 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_projecimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='{{MEDIA_URL}}images/')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='ProjecImage',
        ),
        migrations.AddField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio.project'),
        ),
    ]
