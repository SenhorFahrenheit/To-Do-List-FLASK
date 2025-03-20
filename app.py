from flask import Flask
from routes.routes import routes  # Importando as rotas
from model import db  # Importando o banco e o modelo

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'  # SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'connect_args': {'check_same_thread': False}}


# Inicializando o banco de dados com a aplicação
db.init_app(app)


# Registrando o Blueprint das rotas
app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

