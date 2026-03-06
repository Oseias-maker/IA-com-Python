api_key = 'SUA CHAVE'

import os
os.environ['GROQ_API_KEY'] = api_key

from langchain_groq import ChatGroq

chat = ChatGroq(model='llama-3.1-8b-instant')

resposta = chat.invoke("Olá, modelo! Quem é você?")
print(resposta.content)

print("!!!!-----SUCESSO-----!!!!")