# Generated by Django 2.2 on 2021-04-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solo_Project_App', '0019_cart_user_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='item_added',
            field=models.ManyToManyField(related_name='user_items', to='Solo_Project_App.User'),
        ),
    ]
