from flask import Blueprint, render_template, request
import json
# Criando um "Blueprint" para agrupar as rotas
routes = Blueprint('routes', __name__)


@routes.route('/', methods=["GET"])
def home():
    from crud import listar_tarefas
    response = listar_tarefas()  # Retorna um JSONResponse do Flask
    tasks = json.loads(response.get_data(as_text=True))  # Converte JSON para lista de dicionários
    return render_template('index.html', tasks=tasks)

@routes.route('/add-task', methods=['GET', 'POST'])
def add_task():
    return render_template("addTasks.html")

@routes.route('/update-task/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    return render_template("updateTasks.html", task_id=task_id)

@routes.route('/delete-task/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    return render_template("deleteTasks.html", task_id=task_id)
