# Generated by Django 5.1.1 on 2024-10-04 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_alter_singleplayergame_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleplayergame',
            name='End',
            field=models.DateField(default=datetime.datetime(2024, 10, 4, 14, 18, 21, 488829, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='singleplayergame',
            name='Start',
            field=models.DateField(default=datetime.datetime(2024, 10, 4, 14, 18, 21, 488829, tzinfo=datetime.timezone.utc)),
        ),
    ]
