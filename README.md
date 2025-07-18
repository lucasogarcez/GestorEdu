# GestorEdu

**GestorEdu** é um sistema para gerenciamento de matrículas escolares desenvolvido em:

- **Front-end:** HTML, CSS e JavaScript  
- **Back-end:** Python com Django  
- **Banco de dados:** PostgreSQL

---

## 🚀 Objetivo

Gerenciar alunos, turmas, disciplinas e matrículas de forma intuitiva e eficiente para escolas de pequeno e médio porte.

---

## 🧱 Estrutura do projeto

```
SistemaDeMatriculas/
├── frontend/         ← CSS, JS e Imagens
├── backend/          ← Projeto Django:
    ├── manage.py
    ├── escola/     ← Configurações do projeto Django
    └── core/       ← App principal (alunos, cursos, matrículas)
├── .env.example      
└── requirements.txt  
```

---

## ⚙️ Tecnologias

- Python 3.12.6
- Django  
- PostgreSQL 16+
- HTML5, CSS3, JavaScript  
- Gunicorn (configuração para produção)

---

## 📅 Planejamento Técnico (5 meses)

### 🔹 Mês 1: Levantamento e estrutura inicial
- [x] Definição dos supostos stakeholders (diretor e coordenador)
- [x] Coleta de requisitos com foco nos módulos:
  - Cadastro e consulta de alunos
  - Gestão de matrículas
  - Registro de frequências
  - Acesso com perfis distintos
- [x] Escolha da stack: `Django + PostgreSQL`
- [x] Estruturação do projeto com:
  - Modelagem inicial do banco de dados
  - Criação do repositório com `.env` e settings organizados

### 🔹 Mês 2: Backend e autenticação
- [x] Implementação dos modelos: `Aluno`, `Curso`, `Matrícula`, `Professor`
- [x] Sistema de login/logout com autenticação Django
- [x] Painel administrativo personalizado
- [x] Configuração da conexão PostgreSQL via rede local
- [x] Permissões por grupo (admin, secretária)

### 🔹 Mês 3: Telas e funcionalidades CRUD
- [ ] Templates com base em `HTML/CSS`
- [ ] CRUD completo de alunos, matrículas e professores com validações
- [ ] Filtros e ordenações por curso, nome, período
- [ ] Interface amigável para uso local (modo intranet)

### 🔹 Mês 4: Entregas, testes e robustez
- [ ] Testes funcionais em múltiplas máquinas via IP local
- [ ] Geração de script `.bat` para rodar servidor automaticamente
- [ ] Configuração de firewall, rede e PostgreSQL remoto
- [ ] Criação de dump `.sql` do banco para restauração

### 🔹 Mês 5: Documentação e entrega final
- [ ] Elaboração de documentação técnica para manutenção
- [ ] Criação de manual do usuário final (cliente)
- [ ] Deploy local

---

## 🧑‍💻 Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/lucasogarcez/SistemaDeMatriculas.git
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
4. Aplique as migrations:
   ```bash
   python manage.py migrate
   ```
5. Crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```
6. Execute o servidor:
   ```bash
   python manage.py runserver
   ```
7. Acesse: [http://localhost:8000](http://localhost:8000)

---

## 🔧 Status: Em desenvolvimento

---

## 📜 Licença

Este projeto está sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.
