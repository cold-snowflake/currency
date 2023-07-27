# Generated by Django 4.2.2 on 2023-07-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_alter_rate_created_alter_rate_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequstResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=185, verbose_name='Path')),
                ('request_method', models.CharField(max_length=50, verbose_name='Request method')),
                ('time', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Time')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
            ],
            options={
                'verbose_name': 'Request Respose Log',
                'verbose_name_plural': 'Request Respose Logs',
            },
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Contact us', 'verbose_name_plural': 'Contact us'},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'verbose_name': 'Rate', 'verbose_name_plural': 'Rates'},
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'verbose_name': 'Source', 'verbose_name_plural': 'Sources'},
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email_from',
            field=models.EmailField(max_length=254, verbose_name='Email from'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.CharField(max_length=250, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=25, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='buy',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Buy'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='currency',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Dollar'), (2, 'Euro')], default=2, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='sell',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Sell'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='source',
            field=models.CharField(max_length=68, verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='source',
            name='source_url',
            field=models.CharField(max_length=255, verbose_name='Source url'),
        ),
    ]
