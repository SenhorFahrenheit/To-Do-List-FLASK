from flask import Blueprint, render_template, request

# Criando um "Blueprint" para agrupar as rotas
routes = Blueprint('routes', __name__)

tasks = [{"id": 1, "title": "Comprar pão"}, {"id": 2, "title": "Estudar Python"}]

@routes.route('/', methods=["GET"])
def home():
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
