# Generated by Django 4.1.5 on 2023-01-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NetworkApp', '0002_profile_bio_profile_picture_alter_profile_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='google_url',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='work_place',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
