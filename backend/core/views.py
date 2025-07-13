from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from core.models import Professor, Curso, Aula, Matricula, Frequencia

## Para teste do sistema
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.conf import settings
import json

# Desativa temporariamente o CSRF (use só pra testes, ideal depois usar token real)
@csrf_exempt
def criar_ou_atualizar_usuario(request):
    # Proteção simples por token na query string (troque pela sua chave secreta)
    token = request.GET.get('token')
    if token != settings.SECRET_KEY:
        return JsonResponse({'erro': 'Acesso negado'}, status=403)

    if request.method != 'POST':
        return JsonResponse({'erro': 'Use POST'}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'erro': 'JSON inválido'}, status=400)

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return JsonResponse({'erro': 'username, email e password são obrigatórios'}, status=400)

    # Tenta pegar o usuário pelo username ou cria um novo
    user, created = User.objects.update_or_create(
        username=username,
        defaults={'email': email}
    )
    user.set_password(password)  # Atualiza a senha
    user.save()

    return JsonResponse({
        'status': 'Criado' if created else 'Atualizado',
        'username': user.username,
        'email': user.email
    })
    
## Fim dos testes

def home(request):
    return render(request, 'core/home.html')

class ProfessorLoginView(LoginView):
    template_name = 'core/professor_login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/professor/dashboard/'

@login_required(login_url='/professor/login/')
def DashboardProfessor(request):
    print(f"Usuário logado: {request.user} (id: {request.user.id})")
    professor = get_object_or_404(Professor, user=request.user)
    cursos = Curso.objects.filter(professor=professor)

    return render(request, 'core/dashboard_professor.html', {'cursos': cursos})

@login_required(login_url='/professor/login/')
def AulasDoCurso(request, curso_id):
    curso = get_list_or_404(Curso, id=curso_id)
    aulas = Aula.objects.filter(curso=curso)

    return render(request, 'core/aulas_do_curso.html', {'curso': curso, 'aulas': aulas})

@login_required(login_url='/professor/login/')
def RegistrarFrequencia(request, curso_id):
    curso = get_list_or_404(Curso, id=curso_id)
    aulas = Aula.objects.filter(curso=curso)

    if request.method == 'POST':
        for aula in aulas:
            matriculas = Matricula.objects.filter(curso=curso)
            for matricula in matriculas:
                presente = request.POST.get(f'presente_{matricula.id}_{aula.id}') == 'on'
                frequencia, created = Frequencia.objects.get_or_create(matricula=matricula, aula=aula)
                frequencia.presente = presente
                frequencia.save()
        return redirect('dashboard_professor')

    return render(request, 'core/registrar_frequencia.html', {'curso': curso, 'aulas': aulas})