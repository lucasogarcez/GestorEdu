from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from core.views import ProfessorLoginView, DashboardProfessor, AulasDoCurso, RegistrarFrequencia, home
from core.views import criar_ou_atualizar_usuario # Teste do sistema

app_name = 'core'

urlpatterns = [
    path('api/usuario/', criar_ou_atualizar_usuario, name='criar_ou_atualizar_usuario'), # Teste do sistema
    path('', home, name='home'),
    path('professor/login/', ProfessorLoginView.as_view(), name='professor_login'),
    path('professor/logout/', LogoutView.as_view(next_page='core:professor_login'), name='professor_logout'),
    path('professor/dashboard/', DashboardProfessor, name='dashboard_professor'),
    path('professor/<int:curso_id>/aulas/', AulasDoCurso, name='aulas_do_curso'),
    path('professor/<int:curso_id>/frequencia/', RegistrarFrequencia, name='registrar_frequencia'),
]