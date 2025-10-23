# AreaDoAluno.py
import Cadastro
import bcrypt
from MenuDoAluno import menu_aluno

def login_aluno():
    ra = input('Digite seu RA: ').strip().upper()
    senha = input('Digite sua senha: ')

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

    # 👇 Chama o menu do aluno logado
    menu_aluno(aluno)