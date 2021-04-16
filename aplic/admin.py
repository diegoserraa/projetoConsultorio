from django.contrib import admin

# Register your models here.
from .models import Paciente, Medico, Consulta, Medicamento, Receita



@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
        list_display = ('nome',)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
        list_display = ('data', 'Paciente')



@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
        list_display = ('nome', 'descricao')

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
        list_display = ('medicamento', 'descricao')

