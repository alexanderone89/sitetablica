# Generated by Django 5.1.4 on 2025-01-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='theme',
            field=models.CharField(blank=True, max_length=100, verbose_name='Тема'),
        ),
    ]