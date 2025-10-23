# MenuDoProfessor.py

from Cadastro import carregar_dados
import gerar_boletim

def lancar_notas():
    print("\n=== Lançar Notas ===")
    ra = input("Digite o RA do aluno: ").strip()
    
    alunos = [u for u in carregar_dados() if u.get("tipo") == "aluno"]
    aluno = next((a for a in alunos if a.get("ra") == ra), None)
    
    if not aluno:
        print("❌ Aluno não encontrado!")
        return
    
    materia = input("Digite a matéria: ").strip()
    try:
        nota = float(input("Digite a nota: "))
    except ValueError:
        print("❌ Nota inválida!")
        return
    
    if "notas" not in aluno:
        aluno["notas"] = {}
    aluno["notas"][materia] = nota
    print(f"✅ Nota registrada: {materia} - {nota}")

def realizar_chamada():
    print("\n=== Realizar Chamada ===")
    ra = input("Digite o RA do aluno: ").strip()
    
    alunos = [u for u in carregar_dados() if u.get("tipo") == "aluno"]
    aluno = next((a for a in alunos if a.get("ra") == ra), None)
    
    if not aluno:
        print("❌ Aluno não encontrado!")
        return
    
    aluno["frequencia"] = aluno.get("frequencia", 0) + 1
    print(f"✅ Chamada registrada para {aluno['nome']} ({aluno['frequencia']} dias)")

def gerar_boletim(professor):
    ra = input("Digite o RA do aluno: ").strip()
    from Cadastro import carregar_dados
    alunos = [u for u in carregar_dados() if u.get("tipo") == "aluno"]
    aluno = next((a for a in alunos if a.get("ra") == ra), None)
    if not aluno:
        print("❌ Aluno não encontrado!")
        return
    from gerar_boletim import gerar_boletim_salvar
    gerar_boletim_salvar(aluno)


def verificar_reclamacoes():

    print("\n=== Reclamações dos Alunos ===")
    try:
        with open("reclamacoes.txt", "r", encoding="utf-8") as f:
            reclamacoes = f.readlines()
    except FileNotFoundError:
        reclamacoes = []
    
    if not reclamacoes:
        print("Nenhuma reclamação registrada.\n")
        return
    
    for i, rec in enumerate(reclamacoes, 1):
        print(f"{i}. {rec.strip()}")
    print()


def menu_professor(professor):
    while True:
        print("==============================")
        print("==== MENU DO PROFESSOR ====")
        print("==============================")
        print("1. Lançar notas dos alunos")
        print("2. Realizar a chamada")
        print("3. Boletim escolar do aluno")
        print("4. Verificar reclamações dos alunos")
        print("5. Voltar ao menu principal")
        print("==============================")

        opcao = input("Escolha qual área deseja acessar (1 a 5): ").strip()

        if opcao == "1":
            lancar_notas()
        elif opcao == "2":
            realizar_chamada()
        elif opcao == "3":
            gerar_boletim(professor)
        elif opcao == "4":
            verificar_reclamacoes()
        elif opcao == "5":
            print("Voltando ao menu principal...\n")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")
