# Generated by Django 4.2.2 on 2023-06-27 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_branch_data_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch_data',
            name='No',
            field=models.CharField(max_length=255),
        ),
    ]
