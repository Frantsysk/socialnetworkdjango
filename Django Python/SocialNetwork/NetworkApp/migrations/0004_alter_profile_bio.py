# Generated by Django 4.1.5 on 2023-01-30 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NetworkApp', '0003_profile_email_profile_facebook_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
