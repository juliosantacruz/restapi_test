# Generated by Django 4.0.6 on 2022-07-18 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_carrers_postulation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='user_photo',
        ),
        migrations.AddField(
            model_name='staff',
            name='profile_photo',
            field=models.URLField(blank=True),
        ),
    ]