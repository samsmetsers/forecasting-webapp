# Generated by Django 5.1.1 on 2024-10-03 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_multiplayergame_game_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multiplayergame',
            old_name='Active Game',
            new_name='Active',
        ),
        migrations.RenameField(
            model_name='multiplayergame',
            old_name='Game host',
            new_name='GameUser',
        ),
        migrations.RenameField(
            model_name='singleplayergame',
            old_name='Active Game',
            new_name='Active',
        ),
        migrations.RenameField(
            model_name='singleplayergame',
            old_name='Game host',
            new_name='GameUser',
        ),
        migrations.RenameField(
            model_name='singleplayergame',
            old_name='Game score',
            new_name='Score',
        ),
    ]
