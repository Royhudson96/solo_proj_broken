# Generated by Django 2.2 on 2021-04-18 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Solo_Project_App', '0021_auto_20210417_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_in_cart', to='Solo_Project_App.User'),
        ),
    ]
