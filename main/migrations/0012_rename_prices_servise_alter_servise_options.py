# Generated by Django 5.1.4 on 2025-01-14 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_prices_delete_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prices',
            new_name='Servise',
        ),
        migrations.AlterModelOptions(
            name='servise',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
    ]