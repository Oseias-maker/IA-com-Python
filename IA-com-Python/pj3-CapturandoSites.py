import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = 'SUA CHAVE'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-8b-instant')

from langchain_community.document_loaders import WebBaseLoader


url = input("\n\nOlá, sou uma IA que te ajuda com quaisquer sites da Web. \n\nInsira a URL do site que deseja analisar: ")
loader = WebBaseLoader(url)
lista_documentos = loader.load()
#print(lista_documentos[0].page_content) #extração de dados do site

documento = ''
for doc in lista_documentos:
    documento = documento + doc.page_content


def resposta_bot(mensagens):
    mensagens_modelo = [('system', 'Em todas as respostas ao usuário você será objetivo com as palavras, será chamado de ConexBot e em todas as suas respostas você terá acesso as informações do site selecionado pelo usuário seguir: {documentos_informados}. Por fim, se o usuário querer encerrar o site, informe para ele digitar a palavra "sair"')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'documentos_informados': documento}).content

print("\n\nOlá! Bem vindo ao seu assistente ConexBot. Como posso te ajudar?",
      '\n\nDigite a palavra "sair" para encerrar o chat a qualquer momento.')

mensagens = []
while True:
    pergunta = input('\nUsuário (você): ')
    if pergunta.lower() == 'sair':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens)
    mensagens.append(('assistant', resposta))
    print(f'\nConexBot: {resposta}')



print("\n\nObrigado por usar o ConexBot!")



