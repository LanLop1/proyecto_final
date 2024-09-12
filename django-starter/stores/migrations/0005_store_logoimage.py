# Generated by Django 5.1 on 2024-09-12 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_home', '0013_alter_image_user'),
        ('stores', '0004_rename_bannerurl_store_dirección_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='logoImage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stores_logo_images', to='a_home.image'),
        ),
    ]
