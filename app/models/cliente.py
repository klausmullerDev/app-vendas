from app import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    
def __repr__(self):
    return f'<Cliente {self.nome}, {self.email}>'
    