# Generated by Django 4.2.4 on 2023-09-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_source_code_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='code_name',
            field=models.CharField(max_length=38, unique=True, verbose_name='Code name'),
        ),
    ]
