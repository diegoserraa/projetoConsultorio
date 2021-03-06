# Generated by Django 2.2.19 on 2021-04-16 16:27

import aplic.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Codigo')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome:')),
                ('descricao', models.TextField(blank=True, max_length=2000, verbose_name='Descricão:')),
            ],
            options={
                'verbose_name': 'Medicamento',
                'verbose_name_plural': 'Medicamentos',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='Cpf:')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome:')),
                ('logradouro', models.CharField(max_length=200, verbose_name='Logradouro:')),
                ('bairro', models.CharField(max_length=200, verbose_name='Bairro:')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade:')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=100, verbose_name='Estado:')),
                ('email', models.EmailField(max_length=200, verbose_name='Email:')),
                ('telefoneComercial', models.CharField(max_length=200, verbose_name='Telefone Comercial:')),
                ('telefoneResidencial', models.CharField(max_length=200, verbose_name='Telefone Residencial:')),
                ('telefoneCelular', models.CharField(max_length=200, verbose_name='Celular:')),
                ('idade', models.IntegerField(verbose_name='Idade:')),
                ('foto', stdimage.models.StdImageField(blank=True, null=True, upload_to=aplic.models.get_file_path, verbose_name='Foto:')),
                ('especialidades', models.CharField(choices=[('Cirurgiao', 'Cirurgiao'), ('Clinico Geral', 'Clinico Geral'), ('Pediatra', 'Pediatra'), ('Cardiologista', 'Cardiologista')], max_length=100, verbose_name='Especialidade:')),
                ('crm', models.CharField(max_length=20, unique=True, verbose_name='CRM:')),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='Cpf:')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome:')),
                ('logradouro', models.CharField(max_length=200, verbose_name='Logradouro:')),
                ('bairro', models.CharField(max_length=200, verbose_name='Bairro:')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade:')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=100, verbose_name='Estado:')),
                ('email', models.EmailField(max_length=200, verbose_name='Email:')),
                ('telefoneComercial', models.CharField(max_length=200, verbose_name='Telefone Comercial:')),
                ('telefoneResidencial', models.CharField(max_length=200, verbose_name='Telefone Residencial:')),
                ('telefoneCelular', models.CharField(max_length=200, verbose_name='Celular:')),
                ('idade', models.IntegerField(verbose_name='Idade:')),
                ('foto', stdimage.models.StdImageField(blank=True, null=True, upload_to=aplic.models.get_file_path, verbose_name='Foto:')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Codigo')),
                ('dtPrimeiraConsulta', models.DateField(verbose_name='Data da Primeira Consulta:')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(blank=True, max_length=2000, verbose_name='Como usar:')),
                ('Medicamento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Medicamento')),
                ('Paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Paciente')),
                ('medico', models.ManyToManyField(to='aplic.Medico')),
            ],
            options={
                'verbose_name': 'Receita',
                'verbose_name_plural': 'Receitas',
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Codigo')),
                ('data', models.DateTimeField(blank=True, help_text='formato DD/MM/AAAA', null=True, verbose_name='Data/Hora Consulta:')),
                ('descricao', models.TextField(blank=True, max_length=2000, verbose_name='Descricao:')),
                ('Paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Paciente')),
                ('medico', models.ManyToManyField(to='aplic.Medico')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
            },
        ),
    ]
