# AreaDoProfessor.py
import Cadastro
from getpass import getpass
import bcrypt

def login_professor():
    email = input('Digite seu e-mail institucional: ').strip().lower()
    senha = getpass('Digite sua senha: ')

    # Carrega todos os usuários
    usuarios = Cadastro.carregar_dados()

    # Filtra apenas professores
    professores = [u for u in usuarios if u.get("tipo") == "professor"]

    # Procura o professor pelo email
    professor = next((u for u in professores if u.get("email").lower() == email), None)

    if not professor:
        print("E-mail inválido! Acesso encerrado.")
        return

    # Verifica a senha (comparando hash)
    senha_hash = professor.get("senha").encode('utf-8')
    if not bcrypt.checkpw(senha.encode('utf-8'), senha_hash):
        print("Senha inválida! Acesso encerrado.")
        return

    # Login bem-sucedido
    print('\n✅ Login de professor bem-sucedido!')
    print('Bem-vindo(a) ao painel do professor.\n')
