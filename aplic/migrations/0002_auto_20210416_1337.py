# Generated by Django 2.2.19 on 2021-04-16 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='Medicamento',
            new_name='medicamento',
        ),
    ]
