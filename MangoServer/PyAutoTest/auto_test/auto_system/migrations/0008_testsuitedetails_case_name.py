# Generated by Django 4.1.5 on 2024-11-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_system', '0007_projectproduct_auto_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsuitedetails',
            name='case_name',
            field=models.CharField(max_length=528, null=True, verbose_name='key'),
        ),
    ]
