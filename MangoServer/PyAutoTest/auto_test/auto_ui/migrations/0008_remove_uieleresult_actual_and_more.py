# Generated by Django 4.1.5 on 2024-10-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_ui', '0007_alter_uipagestepsdetailed_ope_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uieleresult',
            name='actual',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='ass_type',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='ass_value',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='ele_quantity',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='error_message',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='expect',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='loc',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='ope_type',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='ope_value',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='picture_path',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='sleep',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='status',
        ),
        migrations.RemoveField(
            model_name='uieleresult',
            name='sub',
        ),
        migrations.RemoveField(
            model_name='uipagestepsdetailed',
            name='ass_type',
        ),
        migrations.RemoveField(
            model_name='uipagestepsdetailed',
            name='ass_value',
        ),
        migrations.RemoveField(
            model_name='uipagestepsdetailed',
            name='ope_type',
        ),
        migrations.AddField(
            model_name='uieleresult',
            name='element_data',
            field=models.JSONField(null=True, verbose_name='元素测试结果'),
        ),
    ]
