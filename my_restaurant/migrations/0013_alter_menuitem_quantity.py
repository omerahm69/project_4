# Generated by Django 4.2.19 on 2025-05-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_restaurant', '0012_restaurant_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
