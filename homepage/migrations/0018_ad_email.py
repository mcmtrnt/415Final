# Generated by Django 2.1.5 on 2019-06-14 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_auto_20190604_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='email',
            field=models.TextField(null=True),
        ),
    ]
