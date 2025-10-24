# Turmas.py
import os

ARQUIVO_TURMAS = "dados/turmas.txt"
ARQUIVO_USUARIOS = "dados/usuarios.txt"


def criar_turma():
    print("\n=== Criar Nova Turma ===")
    nome_turma = input("Nome da turma (ex: ADS2025-A): ").strip().upper()
    curso = input("Curso: ").strip().title()
    semestre = input("Semestre (ex: 1º, 2º): ").strip()

    if not os.path.exists(ARQUIVO_TURMAS):
        open(ARQUIVO_TURMAS, "w", encoding="utf-8").close()

    with open(ARQUIVO_TURMAS, "r", encoding="utf-8") as f:
        for linha in f:
            if nome_turma in linha:
                print("❌ Essa turma já existe!")
                return

    with open(ARQUIVO_TURMAS, "a", encoding="utf-8") as f:
        f.write(f"{nome_turma};{curso};{semestre};[];[]\n")  

    print(f"✅ Turma {nome_turma} criada com sucesso!")

# =====================================================
# Função para listar turmas
# =====================================================
def listar_turmas():
    print("\n=== Lista de Turmas ===")
    if not os.path.exists(ARQUIVO_TURMAS) or os.path.getsize(ARQUIVO_TURMAS) == 0:
        print("Nenhuma turma cadastrada.")
        return

    with open(ARQUIVO_TURMAS, "r", encoding="utf-8") as f:
        for linha in f:
            nome, curso, semestre, alunos, profs = linha.strip().split(";")
            print(f"📘 {nome} | {curso} | {semestre} semestre")
            print(f"  👨‍🎓 Alunos: {alunos}")
            print(f"  👨‍🏫 Professores: {profs}")
            print("------------------------------")

# =====================================================
# Adicionar aluno ou professor a uma turma
# =====================================================
def adicionar_usuario_turma():
    listar_turmas()
    turma_nome = input("\nDigite o nome da turma para associar o usuário: ").strip().upper()
    tipo = input("Adicionar (aluno/professor): ").strip().lower()
    email = input("E-mail do usuário: ").strip().lower()

    if not os.path.exists(ARQUIVO_USUARIOS):
        print("❌ Nenhum usuário cadastrado ainda!")
        return

    # Verifica se o usuário existe e é do tipo correto
    usuario_encontrado = False
    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
        for linha in f:
            tipo_user, nome, email_user, cpf, senha = linha.strip().split(";")
            if tipo_user == tipo and email_user == email:
                usuario_encontrado = True
                usuario_nome = nome
                break

    if not usuario_encontrado:
        print(f"❌ Nenhum {tipo} encontrado com esse e-mail.")
        return

    # Atualiza o arquivo de turmas
    linhas_novas = []
    turma_encontrada = False
    with open(ARQUIVO_TURMAS, "r", encoding="utf-8") as f:
        for linha in f:
            nome, curso, semestre, alunos, profs = linha.strip().split(";")
            if nome == turma_nome:
                turma_encontrada = True
                if tipo == "aluno":
                    if usuario_nome in alunos:
                        print("⚠️ Aluno já está nessa turma.")
                    else:
                        alunos = alunos.replace("]", f", {usuario_nome}]") if alunos != "[]" else f"[{usuario_nome}]"
                        print(f"✅ {usuario_nome} adicionado à turma {turma_nome}.")
                elif tipo == "professor":
                    if usuario_nome in profs:
                        print("⚠️ Professor já está nessa turma.")
                    else:
                        profs = profs.replace("]", f", {usuario_nome}]") if profs != "[]" else f"[{usuario_nome}]"
                        print(f"✅ Professor {usuario_nome} vinculado à turma {turma_nome}.")
                linha = f"{nome};{curso};{semestre};{alunos};{profs}\n"
            linhas_novas.append(linha)

    if not turma_encontrada:
        print("❌ Turma não encontrada.")
        return

    with open(ARQUIVO_TURMAS, "w", encoding="utf-8") as f:
        f.writelines(linhas_novas)

# =====================================================
# Menu da área de turmas
# =====================================================
def menu_turmas():
    while True:
        print("\n=== MENU DE TURMAS ===")
        print("1. Criar nova turma")
        print("2. Listar turmas")
        print("3. Adicionar aluno/professor a turma")
        print("4. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_turma()
        elif opcao == "2":
            listar_turmas()
        elif opcao == "3":
            adicionar_usuario_turma()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")
