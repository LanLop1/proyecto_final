# Generated by Django 5.1 on 2024-08-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_home', '0003_order_product_store_subscriptionplan_template_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imageurl',
        ),
        migrations.RemoveField(
            model_name='qrcode',
            name='qrcodeurl',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='planname',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.TextField(unique=True),
        ),
    ]
