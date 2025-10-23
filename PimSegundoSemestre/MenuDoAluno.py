# MenuDoAluno.py

from Cadastro import carregar_dados
import gerar_boletim

def ver_boletim(aluno):
    from gerar_boletim import gerar_boletim_salvar
    gerar_boletim_salvar(aluno)


def menu_aluno(aluno):
    while True:
        print("==============================")
        print("==== MENU DO ALUNO ====")
        print("==============================")
        print("1. Ver boletim escolar")
        print("2. Ver notas por matéria")
        print("3. Ver frequência")
        print("4. Enviar reclamação")
        print("5. Voltar ao menu principal")
        print("==============================")

        opcao = input("Escolha qual área deseja acessar (1 a 4): ").strip()

        if opcao == "1":
            ver_boletim(aluno)
        elif opcao == "2":
            notas = aluno.get("notas", {})
            if notas:
                print("\n📘 Notas do aluno:")
                for materia, nota in notas.items():
                    print(f"{materia}: {nota}")
            else:
                print("\nNenhuma nota registrada.")
        elif opcao == "3":
            frequencia = aluno.get("frequencia", 0)
            print(f"\n📅 Frequência: {frequencia} dias")
        elif opcao == "4":
            enviar_reclamacao(aluno)
        elif opcao == "5":
            print("Voltar ao menu principal")
            break
        else:
            print("❌ ERRO! Escolha uma das opções válidas (1 a 4).")


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
