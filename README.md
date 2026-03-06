# 🤖 HelpBot – Assistente Virtual em Python

## 📌 Descrição do Projeto

O **HelpBot** é um assistente virtual simples desenvolvido em **Python** que funciona diretamente no terminal.
O projeto utiliza um **modelo de linguagem baseado em IA** para responder perguntas do usuário de forma amigável e objetiva.

A aplicação mantém um histórico da conversa durante a execução, permitindo que o assistente responda de forma contextualizada.

Este projeto demonstra o uso de **modelos de linguagem (LLM)** integrados ao Python através da biblioteca **LangChain**.

---

## 🎯 Objetivo

O objetivo deste projeto é demonstrar:

* Integração de **Modelos de Linguagem (LLM)** em aplicações Python
* Uso da biblioteca **LangChain** para construção de prompts
* Criação de um **chat interativo no terminal**
* Manipulação de **histórico de conversas**
* Integração com a **API Groq**

Este projeto pode ser utilizado como base para sistemas mais complexos, como **chatbots, assistentes virtuais ou sistemas de suporte automatizado**.

---

## ⚙️ Tecnologias Utilizadas

* **Python**
* **LangChain**
* **Groq API**
* **LLM Llama 3.1 8B**

Bibliotecas principais utilizadas:

```
langchain
langchain_groq
os
```

---

## 📂 Funcionamento do Projeto

O programa funciona da seguinte maneira:

1. Define a **chave da API Groq** no ambiente do sistema.
2. Inicializa um **modelo de linguagem (LLM)**.
3. Define um **prompt de sistema**, instruindo o modelo a agir como um assistente amigável.
4. Inicia um **loop de conversa no terminal**.
5. Cada pergunta do usuário é adicionada ao **histórico de mensagens**.
6. O histórico é enviado ao modelo, que gera uma resposta.
7. A conversa continua até o usuário digitar **"sair"**.

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```
git clone https://github.com/seu-usuario/helpbot.git
```

### 2️⃣ Acessar a pasta do projeto

```
cd helpbot
```

### 3️⃣ Instalar as dependências

```
pip install langchain langchain-groq
```

### 4️⃣ Executar o programa

```
python helpbot.py
```

---

## 💬 Exemplo de Uso

```
Olá! Bem vindo ao seu assistente HelpBot.
Digite a palavra "sair" para encerrar o chat a qualquer momento.

Usuário (você): O que é inteligência artificial?

HelpBot: Inteligência artificial é um campo da computação que desenvolve sistemas capazes de realizar tarefas que normalmente exigiriam inteligência humana.

Usuário (você): sair

Obrigado por usar o HelpBot!
```

---

## 🧠 Conceitos Demonstrados

Este projeto aborda conceitos importantes como:

* **Prompt Engineering**
* **LLMs (Large Language Models)**
* **Chatbots em Python**
* **Gerenciamento de contexto de conversa**
* **Integração com APIs de IA**

---

## 🚀 Possíveis Melhorias

Algumas melhorias que podem ser implementadas no projeto:

* Criar uma **interface web com Flask ou Streamlit**
* Implementar **memória persistente das conversas**
* Adicionar **tratamento de erros da API**
* Permitir **configuração dinâmica do modelo**
* Integrar com **bancos de dados ou sistemas externos**

---

## 👨‍💻 Autor

Projeto desenvolvido para fins de estudo e prática em **Inteligência Artificial aplicada com Python**.
