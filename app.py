# from flask import Flask
# from routes.routes import routes  # Importando as rotas
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Configuração do banco de dados
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'  # SQLite
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Tarefa(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     titulo = db.Column(db.String(100), nullable=False)
#     descricao = db.Column(db.Text, nullable=True)
#     concluida = db.Column(db.Boolean, default=False)

#     def __repr__(self):
#         return f'<Tarefa {self.titulo}>'



# # Registrando o Blueprint das rotas
# app.register_blueprint(routes)



# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)

from flask import Flask
from routes.routes import routes  # Importando as rotas
from model import db  # Importando o banco e o modelo

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'  # SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o banco de dados com a aplicação
db.init_app(app)


# Registrando o Blueprint das rotas
app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

