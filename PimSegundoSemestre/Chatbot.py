# Chatbot.py
import AreaDoAluno
import AreaDoProfessor
import Cadastro

def chatbot():
    print("\n Olá! Eu sou o Chatbot da Faculdade.")
    print("Posso ajudar com login, cadastro, informações e muito mais!")
    print("Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Você: ").strip().lower()

        # ======= SAIR =======
        if pergunta in ["sair", "tchau", "adeus"]:
            print("Chatbot: Até logo! Bons estudos! 👋")
            break

        # ======= LOGIN =======
        elif "login" in pergunta:
            if "professor" in pergunta:
                print("Chatbot: Ok! Vamos fazer o login como professor 👨‍🏫")
                AreaDoProfessor.login_professor()
            elif "aluno" in pergunta:
                print("Chatbot: Ok! Vamos fazer o login como aluno 🎓")
                AreaDoAluno.login_aluno()
            else:
                print("Chatbot: Você quer fazer login como professor ou aluno?")

        # ======= CADASTRO =======
        elif "cadastro" in pergunta or "cadastrar" in pergunta:
            print("Chatbot: Posso ajudar com o cadastro. 👨‍💻")
            print("Quem você deseja cadastrar? (professor / aluno / admin)")
            tipo = input("Você: ").strip().lower()

            if tipo in ["professor", "aluno", "admin"]:
                Cadastro.cadastrar_usuario(tipo)
            else:
                print("Chatbot: Tipo de usuário inválido. Tente novamente.")

       

        elif "nota" in pergunta or "notas" in pergunta:
            print("Chatbot: As notas ficam disponíveis na área do aluno após o login.")
        elif "senha" in pergunta:
            print("Chatbot: Se esqueceu sua senha, peça ajuda ao administrador para redefinir.")
        elif "horário" in pergunta or "aula" in pergunta:
            print("Chatbot: Os horários das aulas estão disponíveis no portal da turma.")
        elif "professor" in pergunta:
            print("Chatbot: Os professores podem lançar notas e consultar alunos pelo sistema.")
        elif "ajuda" in pergunta or "duvida" in pergunta:
            print("Chatbot: Posso ajudar com login, cadastro, notas e acesso ao sistema. O que deseja?")
        elif "sistema" in pergunta:
            print("Chatbot: Este sistema permite gerenciar alunos, professores, notas e turmas.")
        elif "admin" in pergunta:
            print("Chatbot: O administrador tem acesso total ao sistema, podendo cadastrar novos usuários.")
        elif "faculdade" in pergunta:
            print("Chatbot: A Faculdade é comprometida com a excelência acadêmica e inovação tecnológica! 🎓")
        else:
            print("Chatbot: Desculpe, não entendi. Pode reformular a pergunta? 🤔")
