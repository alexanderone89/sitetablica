# Generated by Django 5.1.4 on 2025-01-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_socials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socials',
            name='logo',
            field=models.ImageField(blank=True, upload_to='social_logos/', verbose_name='Логотип'),
        ),
    ]
