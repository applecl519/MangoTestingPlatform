# Generated by Django 4.1.5 on 2023-11-03 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auto_ui', '0015_uieleresult_ass_type_uieleresult_ass_value_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uipagestepsdetailed',
            name='debug_data',
        ),
        migrations.AddField(
            model_name='uipagestepsdetailed',
            name='type',
            field=models.SmallIntegerField(null=True, verbose_name='操作类型'),
        ),
    ]
