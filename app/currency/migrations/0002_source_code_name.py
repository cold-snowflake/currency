# Generated by Django 4.2.4 on 2023-09-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='code_name',
            field=models.CharField(default=1, max_length=38, verbose_name='Code name'),
            preserve_default=False,
        ),
    ]