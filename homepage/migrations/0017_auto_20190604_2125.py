# Generated by Django 2.1.5 on 2019-06-05 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_subscription_subscription_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='subscription_id',
        ),
        migrations.AddField(
            model_name='pros',
            name='subscription_id',
            field=models.TextField(default=None, null=True),
        ),
    ]
