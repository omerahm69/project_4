# Generated by Django 4.2.19 on 2025-05-13 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_restaurant', '0011_remove_restaurant_banner_alter_restaurant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='banners/'),
        ),
    ]
