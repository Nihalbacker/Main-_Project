# Generated by Django 3.2.24 on 2024-04-15 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ref_app', '0003_auto_20240415_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_table',
            name='feedback',
            field=models.CharField(max_length=500),
        ),
    ]
