# Generated by Django 2.2 on 2021-04-23 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Solo_Project_App', '0027_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='Solo_Project_App.User'),
        ),
    ]
