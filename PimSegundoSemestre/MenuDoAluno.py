from Cadastro import carregar_dados
import gerar_boletim

def menu_aluno(aluno):
    while True:
        print("\n==============================")
        print("==== MENU DO ALUNO ====")
        print("==============================")
        print("1. Ver boletim escolar")
        print("2. Ver notas por matéria")
        print("3. Ver frequência")
        print("4. Enviar reclamação")
        print("5. Voltar ao menu principal")
        print("==============================")

        opcao = input("Escolha qual área deseja acessar (1 a 5): ").strip()

        if opcao == "1":
            ver_boletim(aluno)
        elif opcao == "2":
            mostrar_notas(aluno)
        elif opcao == "3":
            mostrar_frequencia(aluno)
        elif opcao == "4":
            enviar_reclamacao(aluno)
        elif opcao == "5":
            print("Voltando ao menu principal...")
            break
        else:
            print("❌ ERRO! Escolha uma das opções válidas (1 a 5).")


def ver_boletim(aluno):
    from gerar_boletim import gerar_boletim_salvar
    gerar_boletim_salvar(aluno)


def mostrar_notas(aluno):
    """
    Exibe as notas do aluno por matéria.
    """
    notas = aluno.get("notas", {})
    if notas:
        print("\n📘 Notas do aluno:")
        for materia, nota in notas.items():
            print(f" - {materia}: {nota}")
        media = sum(notas.values()) / len(notas)
        print(f"\n🧮 Média geral: {media:.2f}")
    else:
        print("\nNenhuma nota registrada.")


def mostrar_frequencia(aluno):
    """
    Exibe a frequência do aluno de forma clara.
    """
    presencas = aluno.get("presencas", 0)
    total_aulas = aluno.get("total_aulas", 100)
    
    if total_aulas == 0:
        print("\n📅 Frequência: Nenhuma aula registrada.")
        return
    
    percentual = (presencas / total_aulas) * 100
    
    print("\n📅 Frequência:")
    print(f" - Presenças: {presencas}/{total_aulas} aulas")
    print(f" - Percentual de presença: {percentual:.1f}%")
    
    # Situação de frequência
    if percentual < 75:
        print("⚠️ Situação: Reprovado por falta")
    else:
        print("✅ Situação: Frequência adequada")


def enviar_reclamacao(aluno):
    """
    Permite ao aluno enviar uma reclamação que será salva em arquivo.
    """
    print("\n=== Enviar Reclamação ===")
    mensagem = input("Digite sua reclamação: ").strip()
    
    if not mensagem:
        print("❌ Reclamação vazia. Operação cancelada.")
        return
    
    with open("reclamacoes.txt", "a", encoding="utf-8") as f:
        f.write(f"{aluno['nome']} ({aluno['ra']}): {mensagem}\n")
    
    print("✅ Reclamação enviada com sucesso!\n")
