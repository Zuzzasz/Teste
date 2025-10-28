# MenuDoProfessor.py
from Cadastro import carregar_dados, salvar_dados
from Cadastro import carregar_dados
import gerar_boletim
from gerar_boletim import gerar_boletim_salvar
import Cadastro

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

def lancar_notas():
    print("\n=== Lançar Notas ===")
    ra = input("Digite o RA do aluno: ").strip()
    
    dados = carregar_dados()
    alunos = [u for u in dados if u.get("tipo") == "aluno"]
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

    # Salva alteração no arquivo principal
    salvar_dados(dados)


from Cadastro import carregar_dados, salvar_dados
from gerar_boletim import gerar_boletim_salvar  # importação direta da função

def realizar_chamada():
    # Carrega todos os usuários
    usuarios = carregar_dados()

    # Filtra apenas alunos
    alunos = [u for u in usuarios if u.get('tipo') == 'aluno']

    if not alunos:
        print("⚠️ Nenhum aluno cadastrado no sistema.")
        return

    print("\n=== REGISTRO DE PRESENÇA (ALUNOS CADASTRADOS) ===\n")

    for aluno in alunos:
        while True:
            resposta = input(f"O aluno {aluno['nome']} (RA: {aluno['ra']}) esteve presente? (s/n): ").strip().lower()
            if resposta in ['s', 'sim']:
                aluno['presencas'] = aluno.get('presencas', 0) + 1
                print(f"✅ Presença registrada para {aluno['nome']}")
                break
            elif resposta in ['n', 'não', 'nao']:
                aluno['faltas'] = aluno.get('faltas', 0) + 1
                print(f"❌ Falta registrada para {aluno['nome']}")
                break
            else:
                print("Resposta inválida! Digite 's' para presente ou 'n' para falta.")

        # Atualiza o total de aulas
        aluno['total_aulas'] = aluno.get('presencas', 0) + aluno.get('faltas', 0)

        # Atualiza o boletim, mas **não imprime**
        gerar_boletim_salvar(aluno, imprimir=False)

    # Salvar alterações no sistema
    salvar_dados(usuarios)
    print("\n✅ Chamada finalizada e dados dos alunos atualizados.\n")

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
            linhas = f.readlines()
    except FileNotFoundError:
        linhas = []
    if not linhas:
        print("Nenhuma reclamação registrada.\n")
        return
    
    reclamacoes_atualizadas = []
    
    for i, linha in enumerate(linhas, 1):
        if '|' in linha:
            reclamacao, resposta = linha.strip().split('|', 1)
        else:
            reclamacao = linha.strip()
            resposta = ""
        
        print(f"{i}. {reclamacao}")
        if resposta:
            print(f"   Resposta: {resposta}")
        else:
            resp = input("Deseja responder a esta reclamação? (s/n): ").strip().lower()
            if resp == 's':
                texto_resposta = input("Digite sua resposta: ").strip()
                resposta = texto_resposta
        
        reclamacoes_atualizadas.append(f"{reclamacao}|{resposta}\n")
    
    with open("reclamacoes.txt", "w", encoding="utf-8") as f:
        f.writelines(reclamacoes_atualizadas)
    
    print("\nReclamações atualizadas com sucesso!\n")
