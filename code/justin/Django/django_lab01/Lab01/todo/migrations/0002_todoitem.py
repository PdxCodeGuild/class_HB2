# Generated by Django 4.1 on 2022-08-19 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='priorities', to='todo.priority')),
            ],
        ),
    ]
