from model import db, Tarefa
from app import app  # Importamos o app do Flask para acessar o contexto

with app.app_context():  # Criando um contexto para acessar o banco
    nova_tarefa = Tarefa(
        titulo='Levar lixo para fora',
        descricao='Preciso pegar o saco de lixo que está na cozinha e levar à lixeira que fica na esquina',
        concluida=False
    )

    db.session.add(nova_tarefa)  # Adiciona ao banco
    db.session.commit()  # Confirma a transação

    print('Tarefa adicionada com sucesso!')
