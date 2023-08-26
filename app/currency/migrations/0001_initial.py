# Generated by Django 4.2.4 on 2023-08-25 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=254, verbose_name='Email from')),
                ('subject', models.CharField(max_length=25, verbose_name='Subject')),
                ('message', models.CharField(max_length=250, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact us',
                'verbose_name_plural': 'Contact us',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Buy')),
                ('sell', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Sell')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('currency', models.PositiveSmallIntegerField(choices=[(1, 'Dollar'), (2, 'Euro')], default=2, verbose_name='Currency')),
                ('source', models.CharField(max_length=68, verbose_name='Source')),
            ],
            options={
                'verbose_name': 'Rate',
                'verbose_name_plural': 'Rates',
            },
        ),
        migrations.CreateModel(
            name='RequstResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=185, verbose_name='Path')),
                ('request_method', models.CharField(default='GET', max_length=50, verbose_name='Request method')),
                ('time', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Time')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
            ],
            options={
                'verbose_name': 'Request Respose Log',
                'verbose_name_plural': 'Request Respose Logs',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.CharField(max_length=255, verbose_name='Source url')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
            },
        ),
    ]
