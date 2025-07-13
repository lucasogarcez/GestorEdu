from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='professor')
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Aula(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data = models.DateTimeField()

    def __str__(self):
        return f"Aula de {self.curso.nome} em {self.data.strftime('%d/%m/%Y %H:%M')}"

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default='ativo')
    
    class Meta:
        unique_together = ('aluno', 'curso')
    
    def __str__(self):
        return f"{self.aluno.nome} matriculado em {self.curso.nome} ({self.status})"
    
class Frequencia(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('matricula', 'aula')

    def __str__(self):
        return f"{self.matricula.aluno.nome} - {self.aula.curso.nome} - {'Presente' if self.presente else 'Ausente'}"