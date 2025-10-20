# main.py
import AreaDoProfessor
import AreaDoAluno
import Chatbot
import Cadastro

print('==============================')
print('    SISTEMA FACULDADE LOGIN')
print('==============================')
print('1. Área do(a) Professor(a)')
print('2. Área do(a) Aluno(a)')
print('3. Chatbot de Dúvidas')
print("4. Cadastro de Novo Usuário")
print('==============================')

opcao = input('Escolha qual área deseja acessar (1, 2, 3 OU 4): ').strip()

if opcao == "1":
    AreaDoProfessor.login_professor()

elif opcao == "2":
    AreaDoAluno.login_aluno()

elif opcao == "3":
    Chatbot.iniciar_chatbot()

elif opcao == "4":
    Cadastro.menu_cadastro()

else:
    print("❌ ERRO! Escolha uma das opções válidas (1, 2, 3 ou 4).")
