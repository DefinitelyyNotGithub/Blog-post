# Generated by Django 4.2.7 on 2024-02-02 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_Post', '0005_usercomments_email_usercomments_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercomments',
            name='sub_comment',
        ),
        migrations.AddField(
            model_name='usercomments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_key', to='Blog_Post.usercomments'),
        ),
    ]
