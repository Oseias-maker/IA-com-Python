import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = 'SUA CHAVE'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-8b-instant')

def resposta_bot(mensagens):
    mensagens_modelo = [('system', 'Você é um assistente amigável e objetivo nas respostas chamado seu assistente virtual')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({}).content

print("\n\nOlá! Bem vindo ao seu assistente HelpBot.",
      '\nDigite a palavra "sair" para encerrar o chat a qualquer momento.')

mensagens = []
while True:
    pergunta = input('\nUsuário (você): ')
    if pergunta.lower() == 'sair':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens)
    mensagens.append(('assistant', resposta))
    print(f'\nHelpBot: {resposta}')



print("\n\nObrigado por usar o HelpBot!")