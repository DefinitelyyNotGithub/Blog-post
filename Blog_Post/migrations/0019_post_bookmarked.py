# Generated by Django 4.2.7 on 2024-03-24 10:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog_Post', '0018_alter_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='BookMarked',
            field=models.ManyToManyField(blank=True, null=True, related_name='bookmarked', to=settings.AUTH_USER_MODEL, verbose_name='bookmarked by '),
        ),
    ]
