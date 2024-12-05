
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.cliente import Cliente
from app.models.funcionario import Funcionario
from app.models.cliente import Cliente
from app.models.produto import Produto
from app.models.itemVenda import ItemVenda
from app.models.venda import Venda


from app import db

# Criação do Blueprint
vendas_bp = Blueprint('vendas', __name__)

@vendas_bp.route('/vendas/novo', methods=['GET', 'POST'])
def registrar_venda():
    if request.method == 'POST':
        funcionario_id = request.form.get('funcionario_id')
        itens = request.form.getlist('itens')  # Lista com os produtos no formato "produto_id-quantidade"

        # Criar a venda
        venda = Venda(funcionario_id=funcionario_id)
        db.session.add(venda)
        db.session.flush()  # Garante que a venda está no banco antes de adicionar itens

        for item in itens:
            try:
                produto_id, quantidade = item.split('-')  # Separar produto_id e quantidade
                produto_id = int(produto_id)
                quantidade_input = int(request.form.get(f'quantidade_{produto_id}', 0))
            except ValueError:
                return "Erro ao processar o item selecionado.", 400

            produto = Produto.query.get(produto_id)
            if not produto:
                return f"Produto com ID {produto_id} não encontrado.", 400

            # Verificar estoque
            if produto.estoque < quantidade_input:
                return f"Estoque insuficiente para o produto {produto.nome}!", 400

            # Criar ItemVenda
            item_venda = ItemVenda(
                venda_id=venda.id,
                produto_id=produto.id,
                quantidade=quantidade_input,
                preco_unitario=produto.preco
            )

            # Atualizar estoque
            produto.estoque -= quantidade_input
            db.session.add(item_venda)

        db.session.commit()
        return redirect(url_for('vendas.listar_vendas'))

    funcionarios = Funcionario.query.all()
    produtos = Produto.query.all()
    return render_template('registrar_venda.html', funcionarios=funcionarios, produtos=produtos)




@vendas_bp.route('/vendas')
def listar_vendas():
    vendas = Venda.query.all()
    return render_template('vendas.html', vendas=vendas)


@vendas_bp.route('/produtos')
def listar_produtos():
    produtos = Produto.query.all()
    return render_template('produtos.html', produtos=produtos)
    
    
@vendas_bp.route('/produtos/novo', methods=('GET', 'POST'))
def adicionar_produto():
    if request.method == 'POST':
        nome = request.form.get('nome')  # Correto
        preco = request.form.get('preco')  # Correto
        estoque = request.form.get('estoque')  # Correto
        
        novo_produto = Produto(nome=nome, preco=preco, estoque=estoque)

        db.session.add(novo_produto)
        db.session.commit()
        
        return redirect(url_for('vendas.listar_produtos'))
    
    return render_template('adicionar_produto.html')

@vendas_bp.route('/produtos/excluir/<int:id>', methods=['POST'])
def excluir_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return redirect(url_for('vendas.listar_produtos'))

    # Excluir o produto
    db.session.delete(produto)
    db.session.commit()

    return redirect(url_for('vendas.listar_produtos'))


# Definição de uma rota simples
@vendas_bp.route('/')
def index():
    return render_template('base.html')

@vendas_bp.route('/funcionarios')
def listar_funcionarios():
    funcionarios = Funcionario.query.all()
    return render_template('funcionarios.html', funcionarios=funcionarios)
    

@vendas_bp.route('/funcionarios/novo', methods=('GET', 'POST'))
def adicionar_funcionario():
    if request.method == 'POST':
        nome = request.form.get('nome')  # Correto
        email = request.form.get('email')  # Correto
        telefone = request.form.get('telefone')  # Correto
        cargo = request.form.get('cargo')  # Correto
        salario = request.form.get('salario')  # Correto
        novo_funcionario = Funcionario(nome=nome, email=email, telefone=telefone, cargo=cargo, salario=salario)

        db.session.add(novo_funcionario)
        db.session.commit()
        
        return redirect(url_for('vendas.listar_funcionarios'))
    
    return render_template('adicionar_funcionario.html')

from flask import flash

@vendas_bp.route('/funcionarios/excluir/<int:id>', methods=['POST'])
def excluir_funcionario(id):
    funcionario = Funcionario.query.get(id)
    
    # Verificar se o funcionário existe
    if not funcionario:
        flash("Funcionário não encontrado.", "danger")  # Mensagem de erro estilizada
        return redirect(url_for('vendas.listar_funcionarios'))

    # Verificar se o funcionário está associado a vendas
    if funcionario.vendas:
        flash(f"O funcionário {funcionario.nome} não pode ser excluído porque está associado a vendas.", "warning")
        return redirect(url_for('vendas.listar_funcionarios'))

    # Excluir o funcionário
    db.session.delete(funcionario)
    db.session.commit()
    flash(f"Funcionário {funcionario.nome} excluído com sucesso!", "success")
    return redirect(url_for('vendas.listar_funcionarios'))


@vendas_bp.route('/clientes')
def listar_clientes():
    clientes = Cliente.query.all()  # Recupera todos os clientes do banco
    return render_template('clientes.html', clientes=clientes)

# Rota para adicionar um novo cliente
@vendas_bp.route('/clientes/novo', methods=['GET', 'POST'])
def adicionar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
        
        # Adiciona ao banco de dados
        db.session.add(novo_cliente)
        db.session.commit()
        
        return redirect(url_for('vendas.listar_clientes'))
    
    return render_template('adicionar_cliente.html')

@vendas_bp.route('/clientes/excluir/<int:id>', methods=['POST'])
def excluir_cliente(id):
    cliente = Cliente.query.get(id)
    if not cliente:
        return redirect(url_for('vendas.listar_clientes'))
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('vendas.listar_clientes'))