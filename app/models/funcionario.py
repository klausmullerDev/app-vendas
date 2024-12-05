from app import db

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(12), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Funcionario {self.nome}, {self.email}>'

