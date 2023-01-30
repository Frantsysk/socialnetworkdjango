# Generated by Django 4.1.5 on 2023-01-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NetworkApp', '0004_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
