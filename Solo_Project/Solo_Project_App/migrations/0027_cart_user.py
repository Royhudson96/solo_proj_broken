# Generated by Django 2.2 on 2021-04-23 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Solo_Project_App', '0026_auto_20210419_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='Solo_Project_App.User'),
        ),
    ]
