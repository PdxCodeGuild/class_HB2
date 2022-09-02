# Generated by Django 4.1 on 2022-08-20 01:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todoitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 8, 20, 1, 49, 49, 929519, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='priority',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
