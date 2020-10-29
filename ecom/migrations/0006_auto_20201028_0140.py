# Generated by Django 3.0.5 on 2020-10-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='pincode',
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
