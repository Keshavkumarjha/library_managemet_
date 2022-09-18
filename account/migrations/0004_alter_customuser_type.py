# Generated by Django 3.2 on 2022-09-18 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_customuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('student', 'STUDENT'), ('admin', 'ADMIN')], default='STUDENT', max_length=11),
        ),
    ]
