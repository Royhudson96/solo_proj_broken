# Generated by Django 2.2 on 2021-04-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solo_Project_App', '0012_auto_20210416_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(related_name='carts', to='Solo_Project_App.Portfolio')),
            ],
        ),
    ]
