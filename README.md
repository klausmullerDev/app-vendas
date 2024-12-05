
---

```markdown
# 🚀 App Vendas

**App Vendas** é uma aplicação web desenvolvida com **Flask**, projetada para gerenciar vendas, produtos, funcionários e clientes de forma eficiente e organizada.

---

## ✨ Funcionalidades

- 🧾 **Cadastro e gerenciamento** de clientes, funcionários e produtos.
- 🛒 **Registro de vendas** associadas a funcionários e produtos.
- 📦 **Controle de estoque** com atualização automática após vendas.
- 📱 **Interface responsiva** utilizando Bootstrap.

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Flask**: Framework Python para desenvolvimento web.
- 🗄️ **SQLite**: Banco de dados leve e integrado.
- 🔄 **SQLAlchemy**: ORM para manipulação do banco de dados.
- 🎨 **Bootstrap**: Framework CSS para estilização responsiva.

---

## ▶️ Como Executar o Projeto

### Pré-requisitos
- Python 3.10 ou superior
- `pip` instalado

### Passos
1. Clone este repositório:
   ```bash
   git clone https://github.com/KlausmullerDev/app-vendas.git
   cd app-vendas
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure o banco de dados:
   ```bash
   flask db init
   flask db migrate -m "Configuração inicial"
   flask db upgrade
   ```

4. Execute o servidor:
   ```bash
   flask run
   ```

5. Acesse em: [http://localhost:5000](http://localhost:5000)

---


## 👨‍💻 Autor

Desenvolvido por **Klaus Muller**. Confira mais projetos em meu [GitHub](https://github.com/KlausmullerDev).

---




