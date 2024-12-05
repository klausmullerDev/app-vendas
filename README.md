# 🌟 App Vendas

**App Vendas** é uma aplicação web robusta e responsiva, construída com **Flask**, para facilitar o gerenciamento de vendas, produtos, funcionários e clientes.

---

## 📋 Funcionalidades Principais

✔️ Cadastro e gerenciamento de **clientes, funcionários e produtos**.  
✔️ Registro completo de **vendas**, vinculando produtos e funcionários.  
✔️ Controle automatizado de **estoque**, com atualização em tempo real.  
✔️ Interface **moderna e responsiva**, com design baseado no **Bootstrap**.

---

## 🚀 Tecnologias

Este projeto utiliza as seguintes tecnologias:

| Tecnologia       | Descrição                         |
|------------------|-----------------------------------|
| **Flask**        | Framework Python para web apps.   |
| **SQLite**       | Banco de dados leve e eficiente.  |
| **SQLAlchemy**   | ORM para manipulação de dados.    |
| **Bootstrap**    | Estilização e responsividade.     |

---

## 🛠️ Como Rodar a Aplicação

Siga estas etapas para configurar e executar o projeto localmente:

### 1️⃣ Pré-requisitos

- **Python** (versão 3.10 ou superior).  
- **`pip`** (gerenciador de pacotes Python).  

### 2️⃣ Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/KlausmullerDev/app-vendas.git
   cd app-vendas
Crie um ambiente virtual e ative-o:
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:
pip install -r requirements.txt
Configure o banco de dados:
flask db init
flask db migrate -m "Configuração inicial"
flask db upgrade
Execute o servidor:
flask run
Acesse no navegador:
http://localhost:5000




Feito com 💻 e ☕ por Klaus Muller.
📂 Confira mais projetos no meu GitHub.

