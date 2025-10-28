# Cadastro.py
import json
import os
import bcrypt
import re
from datetime import datetime

ARQUIVO_USUARIOS = "usuarios.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_dados(dados):
    with open(ARQUIVO_USUARIOS, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def validar_senha(senha):
    if (len(senha) < 8 or
        not re.search(r"[A-Z]", senha) or
        not re.search(r"[a-z]", senha) or
        not re.search(r"\d", senha) or
        not re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/\\|]", senha)):
        return False
    return True

def pedir_senha_segura():
    while True:
        senha = input("Digite uma senha forte: ")
        if validar_senha(senha):
            return senha
        print("❌ Senha fraca. Regras:\n"
              "- Mínimo 8 caracteres\n"
              "- Uma letra maiúscula\n"
              "- Uma letra minúscula\n"
              "- Um número\n"
              "- Um símbolo (!@#$%)\n")

def menu_cadastro():
    while True:
        print("\n==============================")
        print("   SISTEMA DE CADASTRO UNIP")
        print("==============================")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Professor")
        print("3. Voltar ao menu principal")
        print("==============================")

        tipo = input("Escolha o tipo de cadastro (1, 2 ou 3): ").strip()

        if tipo == "1":
            cadastrar_aluno()
        elif tipo == "2":
            cadastrar_professor()
        elif tipo == "3":
            print("🔙 Voltando ao menu principal...")
            break
        else:
            print("❌ Opção inválida. Escolha uma das opções corretas.")

def cadastrar_aluno():
    dados = carregar_dados()

    print("\n=== Cadastro de Aluno ===")
    nome = input("Nome do aluno: ").strip()
    ra = input("RA do aluno: ").strip().upper()
    email = input("E-mail do aluno: ").strip().lower()
    idade = int(input("Idade: "))

    # Verifica se RA ou e-mail já existem
    if any(u for u in dados if u.get("ra") == ra):
        print("❌ RA já cadastrado!")
        return
    if any(u for u in dados if u.get("email", "").lower() == email):
        print("❌ E-mail já cadastrado!")
        return

    senha = pedir_senha_segura()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    agora = datetime.now().isoformat()
    aluno = {
        "tipo": "aluno",
        "nome": nome,
        "ra": ra,
        "idade": idade,
        "email": email,
        "senha": senha_hash.decode('utf-8'),
        "acessos": [agora],
        "tempo_total_minutos": 0,
        "notas": {},
        "presencas": 0,
        "total_aulas": 0
    }

    # Salva o aluno no sistema
    dados.append(aluno)
    salvar_dados(dados)
    print("✅ Aluno cadastrado com sucesso!\n")

def cadastrar_professor():
    dados = carregar_dados()  # <- colocar aqui no começo

    print("\n=== Cadastro de Professor ===")
    nome = input("Nome do professor: ")
    email = input("E-mail institucional: ").strip().lower()
    disciplina = input("Disciplina que leciona: ")
    idade = int(input("Idade: "))

    # Verifica se e-mail já existe
    if any(u for u in dados if u.get("email","").lower() == email.lower()):
        print("❌ E-mail já cadastrado!")
        return

    senha = pedir_senha_segura()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    agora = datetime.now().isoformat()
    professor = {
        "tipo": "professor",
        "nome": nome,
        "idade": idade,
        "email": email,
        "disciplina": disciplina,
        "senha": senha_hash.decode('utf-8'),
        "acessos": [agora],
        "tempo_total_minutos": 0
    }

    dados.append(professor)
    salvar_dados(dados)
    print("✅ Professor cadastrado com sucesso!\n")


def cadastrar_usuario(tipo):
    if tipo == "aluno":
        cadastrar_aluno()
    elif tipo == "professor":
        cadastrar_professor()

def carregar_dados_alunos():
    if not os.path.exists("alunos.json"):
        return []
    with open("alunos.json", "r", encoding="utf-8") as f:
        return json.load(f)

def carregar_dados_professores():
    if not os.path.exists("professores.json"):
        return []
    with open("professores.json", "r", encoding="utf-8") as f:
        return json.load(f)
