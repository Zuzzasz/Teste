# main.py
import AreaDoAluno
import Cadastro
import gerar_boletim
import Chatbot 
import AreaDoProfessor


def menu_principal():
    while True:
        print('\n==============================')
        print('    SISTEMA FACULDADE LOGIN')
        print('==============================')
        print('1. Área do(a) Professor(a)')
        print('2. Área do(a) Aluno(a)')
        print('3. Chatbot de Dúvidas')
        print('4. Cadastro de Novo Usuário')
        print('5. Sair')
        print('==============================')

        opcao = input('\nEscolha qual área deseja acessar (1, 2, 3, 4 ou 5): ').strip()

        if opcao == "1":
            AreaDoProfessor.login_professor()
        elif opcao == "2":
            AreaDoAluno.login_aluno()
        elif opcao == "3":
            Chatbot.iniciar_chatbot()
        elif opcao == "4":
            Cadastro.menu_cadastro()  # chama menu de cadastro
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("❌ ERRO! Escolha uma das opções válidas (1 a 5).")

if __name__ == "__main__":
    menu_principal()
