# Generated by Django 5.0.3 on 2024-04-15 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_ui', '0035_uipagestepsdetailed_key_uipagestepsdetailed_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uielement',
            name='locator',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='ele_name_a',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='ele_name_b',
        ),
        migrations.RemoveField(
            model_name='uipagestepsdetailed',
            name='ele_name_a',
        ),
        migrations.RemoveField(
            model_name='uipagestepsdetailed',
            name='ele_name_b',
        ),
        migrations.AddField(
            model_name='uieleresult',
            name='ele_name',
            field=models.CharField(max_length=64, null=True, verbose_name='元素名称'),
        ),
        migrations.AddField(
            model_name='uipagestepsdetailed',
            name='ele_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uielement'),
        ),
    ]
