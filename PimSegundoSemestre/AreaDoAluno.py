# AreaDoAluno.py
import Cadastro
from getpass import getpass
import bcrypt

def login_aluno():
    ra = input('Digite seu RA: ').strip().upper()
    senha = getpass('Digite sua senha: ')

    # Carrega todos os usuários
    usuarios = Cadastro.carregar_dados()

    # Filtra apenas alunos
    alunos = [u for u in usuarios if u.get("tipo") == "aluno"]

    # Procura o aluno pelo RA
    aluno = next((u for u in alunos if u.get("ra") == ra), None)

    if not aluno:
        print("RA inválido! Acesso encerrado.")
        return

    # Verifica a senha (comparando hash)
    senha_hash = aluno.get("senha").encode('utf-8')
    if not bcrypt.checkpw(senha.encode('utf-8'), senha_hash):
        print("Senha inválida! Acesso encerrado.")
        return

    # Login bem-sucedido
    print('\n✅ Login de aluno bem-sucedido!')
    print('Bem-vindo(a) ao portal do aluno.\n')
