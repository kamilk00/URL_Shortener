# Generated by Django 4.0.3 on 2022-12-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URL_Shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortenedurl',
            name='shortened',
            field=models.URLField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
