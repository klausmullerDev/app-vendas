from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'minha-chave-secreta'

    # Corrigir a URL do banco de dados para o formato correto
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    print("Caminho do banco de dados:", app.config['SQLALCHEMY_DATABASE_URI'])


    db.init_app(app)

    # Registrar Blueprints
    from .routes.vendas import vendas_bp
    app.register_blueprint(vendas_bp)

    return app
