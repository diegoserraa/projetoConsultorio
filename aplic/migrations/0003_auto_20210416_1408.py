# Generated by Django 2.2.19 on 2021-04-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_auto_20210416_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='facebook',
            field=models.CharField(blank=True, max_length=200, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='medico',
            name='instagran',
            field=models.CharField(blank=True, max_length=200, verbose_name='Instagran'),
        ),
        migrations.AddField(
            model_name='medico',
            name='twitter',
            field=models.CharField(blank=True, max_length=200, verbose_name='Twitter'),
        ),
    ]
