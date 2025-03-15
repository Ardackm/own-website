# Generated by Django 5.1.6 on 2025-02-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright_text', models.CharField(default='© 2025 Tüm hakları saklıdır.', max_length=200)),
            ],
            options={
                'verbose_name': 'Footer İçeriği',
                'verbose_name_plural': 'Footer İçeriği',
            },
        ),
    ]
