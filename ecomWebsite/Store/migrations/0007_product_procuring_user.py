# Generated by Django 4.0.4 on 2022-07-19 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_userprofile'),
        ('Store', '0006_alter_product_brand_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='procuring_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='User.userprofile'),
        ),
    ]
