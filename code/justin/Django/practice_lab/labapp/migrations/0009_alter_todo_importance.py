# Generated by Django 4.1 on 2022-08-26 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0008_alter_todo_importance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='importance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='labapp.priority'),
        ),
    ]