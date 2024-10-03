# Generated by Django 5.1.1 on 2024-10-03 16:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_multiplayergame_difficulty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiplayergame',
            name='game_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='singleplayergame',
            name='game_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
