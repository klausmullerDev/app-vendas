from app import db

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=False)
    data = db.Column(db.DateTime, nullable=False, default=db.func.now())

    # Relacionamento com itens de venda
    itens = db.relationship('ItemVenda', backref='venda', lazy=True)

    funcionario = db.relationship('Funcionario', backref='vendas')

    def __repr__(self):
        return f'<Venda {self.id} - Funcionario {self.funcionario.nome}>'
