# Generated by Django 4.1.7 on 2024-10-18 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slog',
            new_name='slug',
        ),
    ]