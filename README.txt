# Teste-Ohmycode

Trata-se de uma api desenvolvida para teste tecnico.

Instruções para executar e testar(windows):

1- Comandos a serem executados no terminal:
ativar venv:
  apiteste> .\teste_env\Scripts\activate
iniciar servidor:
  apiteste> python .\manage.py runserver

2 -  Fazer login
usuarios já criados:
username:admin
senha:123

username:joao
senha:123

username:jose
senha:123

URL de login:
(painel admin django) http://127.0.0.1:8000/admin/
(Django Rest Framework login) http://127.0.0.1:8000/auth/login

3- Acessar endpoints.

ENDPOINTS:
Get e Post:
http://127.0.0.1:8000/api/v1/tasks/ 

Put e Delete:
http://127.0.0.1:8000/api/v1/tasks/(task id)

Mostrar as tasks do usuário atualmente logado: 
http://127.0.0.1:8000/api/v1/users/tasks
