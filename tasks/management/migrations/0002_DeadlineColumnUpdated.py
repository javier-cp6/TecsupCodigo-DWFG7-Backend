# Generated by Django 4.0.6 on 2022-07-21 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_CreateTableTasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(db_column='task_deadline'),
        ),
    ]
