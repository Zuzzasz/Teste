from MenuDoProfessor import menu_professor
import Cadastro
import bcrypt

def login_professor():
    email = input('Digite seu e-mail institucional: ').strip().lower()
    senha = input('Digite sua senha: ')

    # Carrega todos os usuários
    usuarios = Cadastro.carregar_dados()

    # Filtra apenas professores
    professores = [u for u in usuarios if u.get("tipo") == "professor"]

    # Procura o professor pelo e-mail
    professor = next((u for u in professores if u.get("email").lower() == email), None)

    if not professor:
        print("E-mail inválido! Acesso encerrado.")
        return

    # Verifica a senha (comparando hash)
    senha_hash = professor.get("senha").encode('utf-8')
    if not bcrypt.checkpw(senha.encode('utf-8'), senha_hash):
        print("Senha inválida! Acesso encerrado.")
        return

    print(f"\n✅ Login de professor bem-sucedido! Bem-vindo(a), {professor.get('nome')}\n")

    # 👇 Chama o menu do professor logado
    menu_professor(professor)
