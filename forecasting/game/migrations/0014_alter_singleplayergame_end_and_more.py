# Generated by Django 5.1.1 on 2024-10-07 21:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_alter_singleplayergame_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleplayergame',
            name='End',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='singleplayergame',
            name='Start',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
