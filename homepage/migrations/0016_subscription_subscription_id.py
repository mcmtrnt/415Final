# Generated by Django 2.1.5 on 2019-06-05 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_auto_20190604_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='subscription_id',
            field=models.TextField(default=None, null=True),
        ),
    ]