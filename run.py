from app import create_app, db
from flask import Flask



app = create_app()
@app.cli.command('clear-db')
def clear_db():
    """Remove todos os dados do banco de dados sem deletar as tabelas."""
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print(f"Limpando tabela {table.name}")
        db.session.execute(table.delete())
    db.session.commit()
    print("Banco de dados limpo com sucesso!")
with app.app_context():
    db.create_all()  # Cria as tabelas no banco de dados

if __name__ == '__main__':
    app.run(debug=True)
