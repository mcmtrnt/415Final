# Generated by Django 2.1.5 on 2019-04-04 23:29

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20190404_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='difference',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='recentads',
            name='difference',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=7, null=True),
        ),
    ]