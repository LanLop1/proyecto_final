# Generated by Django 5.1 on 2024-09-12 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_home', '0013_alter_image_user'),
        ('products', '0004_alter_product_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_images_2', to='a_home.image'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_images_3', to='a_home.image'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_images_4', to='a_home.image'),
        ),
    ]
