# Generated by Django 4.0.4 on 2022-07-10 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_alter_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_descp',
            field=models.CharField(max_length=15000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image_main',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(null=True),
        ),
    ]
