# Generated by Django 4.2.18 on 2025-02-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_restaurant', '0004_remove_restaurant_image_menuitem_banner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.TextField(default='3'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.CharField(default='default.jpg', max_length=2083),
        ),
    ]
