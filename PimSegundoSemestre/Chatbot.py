# Chatbot.py

def iniciar_chatbot():
    print('\nOlá! Sou o Chatbot da UNIP.')
    print('Posso ajudar com horários, professores ou dúvidas gerais.')
    print('Digite "sair" para encerrar.\n')

    while True:
        pergunta = input('Você: ').strip().lower()

        if pergunta in ['sair', 'encerrar', 'tchau']:
            print('Chatbot: Até logo!')
            break

        elif 'horário' in pergunta or 'aula' in pergunta:
            print('Chatbot: As aulas começam às 19h10 e vão até as 22h00.')

        elif 'professor' in pergunta or 'contato' in pergunta:
            print('Chatbot: Envie mensagem pelo portal do aluno para falar com seu professor.')

        elif 'dúvida' in pergunta or 'ajuda' in pergunta:
            print('Chatbot: Você pode acessar o fórum de dúvidas ou mandar e-mail para suporte@unip.com.')

        else:
            print('Chatbot: Desculpe, não entendi. Pode reformular sua pergunta?')
