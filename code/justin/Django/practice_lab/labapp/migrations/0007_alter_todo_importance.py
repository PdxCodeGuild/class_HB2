# Generated by Django 4.1 on 2022-08-26 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0006_alter_todo_importance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='importance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labapp.priority'),
        ),
    ]
