# Generated by Django 4.1.5 on 2023-02-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NetworkApp', '0005_post_like_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_pictures/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_pictures/'),
        ),
    ]