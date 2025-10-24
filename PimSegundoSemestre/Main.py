# main.py
import AreaDoAluno
import AreaDoProfessor
import Cadastro
import gerar_boletim
import Chatbot 
import Turmas

def menu_principal():
    while True:
        print('\n==============================')
        print('    SISTEMA FACULDADE LOGIN')
        print('==============================')
        print('1. Área do(a) Professor(a)')
        print('2. Área do(a) Aluno(a)')
        print('3. Chatbot de Dúvidas')
        print('4. Cadastro de Novo Usuário')
        print("5. Acessar turmas ")
        print('6. Sair')
        print('==============================')

        opcao = input('\nEscolha qual área deseja acessar (1 a 6): ').strip()

        if opcao == "1":
            AreaDoProfessor.login_professor()
        elif opcao == "2":
            AreaDoAluno.login_aluno()
        elif opcao == "3":
            Chatbot.chatbot()
        elif opcao == "4":
            Cadastro.menu_cadastro()  
        elif opcao == "5":
            Turmas.menu_turmas()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("❌ ERRO! Escolha uma das opções válidas (1 a 6).")

if __name__ == "__main__":
    menu_principal()
