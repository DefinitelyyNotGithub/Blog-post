# Generated by Django 4.2.7 on 2024-02-27 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_Post', '0015_alter_usercomments_email_alter_usercomments_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercomments',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usercomments',
            name='name',
        ),
        migrations.RemoveField(
            model_name='usercomments',
            name='subject',
        ),
    ]
