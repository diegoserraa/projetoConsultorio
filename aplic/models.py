from django.db import models

# Create your models here.

from django.db import models
from stdimage.models import StdImageField
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Pessoa(models.Model):
    cpf = models.CharField('Cpf:', max_length=11, unique=True)
    nome = models.CharField('Nome:', max_length=200)
    logradouro = models.CharField('Logradouro:', max_length=200)
    bairro = models.CharField('Bairro:', max_length=200)
    cidade = models.CharField('Cidade:', max_length=200)
    OPCOES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    estado = models.CharField('Estado:', max_length=100, choices=OPCOES)
    email = models.EmailField('Email:', max_length=200)
    telefoneComercial = models.CharField('Telefone Comercial:', max_length=200)
    telefoneResidencial = models.CharField('Telefone Residencial:', max_length=200)
    telefoneCelular = models.CharField('Celular:', max_length=200)
    idade = models.IntegerField('Idade:')
    foto = StdImageField('Foto:', null=True, blank=True, upload_to=get_file_path,
                         variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class Paciente(Pessoa):
    codigo = models.IntegerField('Codigo', unique=True)
    dtPrimeiraConsulta = models.DateField('Data da Primeira Consulta:')

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Medico(Pessoa):
    OPCOES = (
        ('Cirurgiao', 'Cirurgiao'),
        ('Clinico Geral', 'Clinico Geral'),
        ('Pediatra', 'Pediatra'),
        ('Cardiologista', 'Cardiologista'),

    )

    especialidades = models.CharField('Especialidade:', max_length=100, choices=OPCOES)
    crm = models.CharField('CRM:', unique=True, max_length=20)
    twitter = models.CharField('Twitter', blank=True, max_length=200)
    facebook = models.CharField('Facebook', blank=True, max_length=200)
    instagran = models.CharField('Instagran', blank=True, max_length=200)

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'





class Consulta(models.Model):
    codigo = models.IntegerField('Codigo', unique=True)
    Paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    medico = models.ManyToManyField(Medico)
    data = models.DateTimeField('Data/Hora Consulta:', blank=True, null=True, help_text='formato DD/MM/AAAA')
    descricao = models.TextField('Descricao:', blank=True, max_length=2000)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

class Medicamento(models.Model):
    codigo = models.IntegerField('Codigo', unique=True)
    nome = models.CharField('Nome:', max_length=200)
    descricao = models.TextField('Descricão:', blank=True, max_length=2000)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'



class Receita(models.Model):
    Paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    medico = models.ManyToManyField(Medico)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.DO_NOTHING)
    descricao = models.TextField('Como usar:', blank=True, max_length=2000)


    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

