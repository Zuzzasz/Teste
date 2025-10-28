# Turmas.py
# Turmas.py
import json
from Cadastro import ARQUIVO_USUARIOS, carregar_dados, salvar_dados  # usa as variáveis e funções do Cadastro
import os

# Caminho do arquivo de turmas (fica no mesmo local do Cadastro.py)
PASTA_PROJETO = os.path.dirname(__file__)
ARQUIVO_TURMAS = os.path.join(PASTA_PROJETO, "turmas.json")

# Garante que o arquivo turmas.json exista
if not os.path.exists(ARQUIVO_TURMAS):
    with open(ARQUIVO_TURMAS, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)

# ========================== FUNÇÕES ==========================

def menu_turmas():
    while True:
        print("\n=== MENU DE TURMAS ===")
        print("1. Criar nova turma")
        print("2. Listar turmas")
        print("3. Adicionar aluno/professor à turma")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            criar_turma()
        elif opcao == "2":
            listar_turmas()
        elif opcao == "3":
            adicionar_usuario_turma()
        elif opcao == "4":
            break
        else:
            print("❌ Opção inválida!")


def criar_turma():
    nome = input("Nome da turma (ex: ADS2025-A): ").strip().upper()
    curso = input("Curso: ").strip()
    semestre = input("Semestre (ex: 1º, 2º): ").strip()

    with open(ARQUIVO_TURMAS, "r", encoding="utf-8") as f:
        turmas = json.load(f)

    for t in turmas:
        if t["nome"] == nome:
            print("❌ Essa turma já existe!")
            return

    nova_turma = {
        "nome": nome,
        "curso": curso,
        "semestre": semestre,
        "alunos": [],
        "professores": []
    }

    turmas.append(nova_turma)
    with open(ARQUIVO_TURMAS, "w", encoding="utf-8") as f:
        json.dump(turmas, f, indent=4)

    print(f"✅ Turma '{nome}' criada com sucesso!\n")


def listar_turmas():
    with open(ARQUIVO_TURMAS, "r", encoding="utf-8") as f:
        turmas = json.load(f)

    if not turmas:
        print("⚠️ Nenhuma turma cadastrada.")
        return []

    for t in turmas:
        print(f"\n📘 Turma: {t['nome']}")
        print(f"📖 Curso: {t['curso']}")
        print(f"🎓 Semestre: {t['semestre']}")
        print(f"👨‍🎓 Alunos: {', '.join(t['alunos']) if t['alunos'] else 'Nenhum'}")
        print(f"👨‍🏫 Professores: {', '.join(t['professores']) if t['professores'] else 'Nenhum'}")
        print("-" * 40)

    return turmas


def adicionar_usuario_turma():
    turmas = listar_turmas()
    if not turmas:
        return

    turma_nome = input("\nDigite o nome da turma: ").strip().upper()
    tipo = input("Adicionar (aluno/professor): ").strip().lower()

    if tipo not in ["aluno", "professor"]:
        print("❌ Tipo inválido. Escolha 'aluno' ou 'professor'.")
        return

    usuarios = carregar_dados()  # usa função do Cadastro.py para ler o arquivo

    usuario_encontrado = None
    if tipo == "aluno":
        ra = input("Digite o RA do aluno: ").strip().upper()
        for u in usuarios:
            if u.get("tipo") == "aluno" and u.get("ra", "").upper() == ra:
                usuario_encontrado = u
                break
    else:
        email = input("Digite o e-mail do professor: ").strip().lower()
        for u in usuarios:
            if u.get("tipo") == "professor" and u.get("email", "").lower() == email:
                usuario_encontrado = u
                break

    if not usuario_encontrado:
        print(f"❌ Nenhum {tipo} encontrado.")
        return

    usuario_nome = usuario_encontrado.get("nome")
    turma_encontrada = False

    for t in turmas:
        if t["nome"] == turma_nome:
            turma_encontrada = True
            lista = t["alunos"] if tipo == "aluno" else t["professores"]
            if usuario_nome in lista:
                print(f"⚠️ {tipo.capitalize()} já está nessa turma.")
            else:
                lista.append(usuario_nome)
                print(f"✅ {tipo.capitalize()} {usuario_nome} adicionado à turma {turma_nome}.")
            break

    if not turma_encontrada:
        print("❌ Turma não encontrada.")
        return

    with open(ARQUIVO_TURMAS, "w", encoding="utf-8") as f:
        json.dump(turmas, f, indent=4)

