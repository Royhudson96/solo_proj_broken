# Generated by Django 2.2 on 2021-04-17 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Solo_Project_App', '0015_auto_20210417_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='cart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='items_in_cart', to='Solo_Project_App.Cart'),
        ),
    ]
