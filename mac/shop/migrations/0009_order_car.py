# Generated by Django 3.2.4 on 2021-07-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_rename_orders_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='car',
            field=models.CharField(default='', max_length=200),
        ),
    ]
