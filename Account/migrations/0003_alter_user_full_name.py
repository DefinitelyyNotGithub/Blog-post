# Generated by Django 4.2.7 on 2023-11-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_remove_user_date_of_birth_user_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='None', max_length=45, unique=True),
        ),
    ]
