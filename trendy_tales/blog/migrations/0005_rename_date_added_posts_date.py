# Generated by Django 5.0 on 2024-01-25 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_posts_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='date_added',
            new_name='date',
        ),
    ]