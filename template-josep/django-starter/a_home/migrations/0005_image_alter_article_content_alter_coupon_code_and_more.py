# Generated by Django 5.1 on 2024-08-19 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_home', '0004_remove_product_imageurl_remove_qrcode_qrcodeurl_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discounttype',
            field=models.TextField(max_length=1255),
        ),
        migrations.AlterField(
            model_name='notification',
            name='readstatus',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=1255),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='store',
            name='bannerurl',
            field=models.TextField(max_length=1255, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='description',
            field=models.TextField(max_length=1255),
        ),
        migrations.AlterField(
            model_name='store',
            name='logourl',
            field=models.TextField(max_length=1255, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='planname',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='a_home.image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_images', to='a_home.image'),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='qr_codes', to='a_home.image'),
        ),
    ]
