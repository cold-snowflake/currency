# Generated by Django 4.2.2 on 2023-07-16 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_source_alter_rate_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='currency',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Dollar'), (2, 'Euro')]),
        ),
    ]