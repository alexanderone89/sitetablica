# Generated by Django 5.1.4 on 2025-01-01 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='cover',
            new_name='image',
        ),
    ]