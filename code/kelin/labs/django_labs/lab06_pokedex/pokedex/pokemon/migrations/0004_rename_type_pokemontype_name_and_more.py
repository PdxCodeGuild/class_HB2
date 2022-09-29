# Generated by Django 4.1 on 2022-09-29 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0003_pokemon_caught_by_pokemontype_pokemon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemontype',
            old_name='type',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='caught_by',
        ),
        migrations.RemoveField(
            model_name='pokemontype',
            name='pokemon',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(related_name='types', to='pokemon.pokemontype'),
        ),
    ]
