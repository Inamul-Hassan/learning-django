# Generated by Django 5.0 on 2024-01-25 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_posts_content_alter_posts_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.author'),
        ),
    ]
