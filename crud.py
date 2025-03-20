from model import db, Tarefa
from app import app  # Importamos o app do Flask para acessar o contexto
from sqlalchemy.exc import SQLAlchemyError

# Criar uma tarefa (C - Create)
def adicionar_tarefa(titulo, descricao, concluida=False):
    with app.app_context():
        try:
            nova_tarefa = Tarefa(titulo=titulo, descricao=descricao, concluida=concluida)
            db.session.add(nova_tarefa)
            db.session.commit()
            print('Tarefa adicionada com sucesso!')
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f'Ocorreu um erro ao adicionar a tarefa: {e}')

# Listar tarefas (R - Read)
def listar_tarefas():
    with app.app_context():
        try:
            tarefas = Tarefa.query.all()
                
            if len(tarefas) <= 0:
                print("Não há tarefas no momento")
                return

            for tarefa in tarefas:
                print(f'{tarefa.id} - {tarefa.titulo} - {tarefa.descricao} - Concluída: {tarefa.concluida}')
        except SQLAlchemyError as e:
            print(f'Ocorreu um erro ao listar as tarefas: {e}')

# Atualizar uma tarefa (U - Update)
def atualizar_tarefa(id, titulo=None, descricao=None, concluida=None):
    with app.app_context():
        try:
            tarefa = db.session.get(Tarefa, id)
            if tarefa:
                if titulo:
                    tarefa.titulo = titulo
                if descricao:
                    tarefa.descricao = descricao
                if concluida is not None:
                    tarefa.concluida = concluida
                db.session.commit()
                print(f'Tarefa {id} atualizada com sucesso!')
            else:
                print(f'Tarefa com ID {id} não encontrada.')
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f'Ocorreu um erro ao atualizar a tarefa: {e}')

# Excluir uma tarefa (D - Delete)
def excluir_tarefa(id):
    with app.app_context():
        try:
            tarefa = db.session.get(Tarefa, id)
            if tarefa:
                db.session.delete(tarefa)
                db.session.commit()
                print(f'Tarefa {id} excluída com sucesso!')
            else:
                print(f'Tarefa com ID {id} não encontrada.')
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f'Ocorreu um erro ao excluir a tarefa: {e}')

# PARA TESTES:

# 1. Adicionando uma nova tarefa
# adicionar_tarefa('Tarefa master', 'Esta é um teste', False)

# 2. Listando todas as tarefas
# listar_tarefas()

# 3. Atualizando uma tarefa (ID da tarefa precisa ser válido)
# atualizar_tarefa(2, descricao='tarefa master foi atualizada', concluida=True)

# 4. Excluindo uma tarefa (ID da tarefa precisa ser válido)
# excluir_tarefa(2)

listar_tarefas()


