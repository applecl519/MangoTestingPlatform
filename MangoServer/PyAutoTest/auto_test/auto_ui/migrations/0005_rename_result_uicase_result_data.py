# Generated by Django 4.1.5 on 2024-11-25 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto_ui', '0004_uicase_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uicase',
            old_name='result',
            new_name='result_data',
        ),
    ]