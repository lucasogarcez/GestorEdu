from django.contrib import admin

from .models import Aluno, Professor, Curso, Aula, Matricula, Frequencia

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1
    
class AulaInline(admin.TabularInline):
    model = Aula
    extra = 1
    
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'professor')
    search_fields = ('nome',)
    inlines = [MatriculaInline, AulaInline]
    
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'email')
    search_fields = ('nome', 'email')
    inlines = [MatriculaInline]
    
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    
@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'data_matricula', 'status')
    search_fields = ('aluno__nome', 'curso__nome')
    list_filter = ('status',)
    
@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('curso', 'data')
    search_fields = ('curso__nome',)
    list_filter = ('data',)

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'aula', 'presente')
    search_fields = ('matricula__aluno__nome', 'aula__curso__nome')
    list_filter = ('presente',)