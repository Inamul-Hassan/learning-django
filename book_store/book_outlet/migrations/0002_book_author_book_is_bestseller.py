# Generated by Django 5.0 on 2024-01-22 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='is_bestseller',
            field=models.BooleanField(default=False),
        ),
    ]