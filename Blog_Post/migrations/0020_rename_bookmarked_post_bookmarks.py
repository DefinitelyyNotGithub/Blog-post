# Generated by Django 4.2.7 on 2024-03-24 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_Post', '0019_post_bookmarked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='BookMarked',
            new_name='BookMarks',
        ),
    ]
