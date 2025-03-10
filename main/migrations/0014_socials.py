# Generated by Django 5.1.4 on 2025-01-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_servise_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='logos/', verbose_name='Логотип')),
                ('url_account', models.CharField(blank=True, max_length=100, verbose_name='Ссылка на аккаунт')),
                ('enabled', models.BooleanField(default=True, verbose_name='Показывать на странице')),
            ],
            options={
                'verbose_name': 'Соцсеть',
                'verbose_name_plural': 'Соцсети',
            },
        ),
    ]
