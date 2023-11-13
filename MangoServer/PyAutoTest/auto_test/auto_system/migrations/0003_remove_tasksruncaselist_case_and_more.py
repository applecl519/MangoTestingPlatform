# Generated by Django 4.1.5 on 2023-10-22 03:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auto_ui', '0007_alter_uiconfig_type'),
        ('auto_system', '0002_database_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasksruncaselist',
            name='case',
        ),
        migrations.RemoveField(
            model_name='tasksruncaselist',
            name='type',
        ),
        migrations.AddField(
            model_name='tasksruncaselist',
            name='ui_case',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uicase'),
        ),
    ]