# Generated by Django 4.0.6 on 2022-07-20 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='task_name', max_length=100)),
                ('description', models.TextField(db_column='task_desc', null=True)),
                ('deadline', models.DateField(db_column='task_deadline')),
                ('status', models.CharField(choices=[('PE', 'Pending'), ('IP', 'In progress'), ('DO', 'Done')], db_column='task_status', default='PE', max_length=2)),
            ],
            options={
                'db_table': 'tasks',
                'ordering': ['-deadline'],
            },
        ),
    ]
