# Generated by Django 4.1.5 on 2023-11-13 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auto_user', '0002_rename_module_name_projectmodule_name'),
        ('auto_ui', '0019_rename_state_uicase_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uipage',
            name='module_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='auto_user.projectmodule'),
        ),
    ]