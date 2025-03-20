from flask import Blueprint, render_template, request, redirect, url_for

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
    from crud import atualizar_tarefa, get_task_by_id
    tarefa = get_task_by_id(task_id)
    
    if not tarefa:
        return "Tarefa não encontrada", 404  # Evita erro ao acessar ID inexistente

    if request.method == "POST":
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        concluida = 'concluida' in request.form  # Se o checkbox estiver marcado, será True; senão, False

        atualizar_tarefa(task_id, titulo, descricao, concluida)

        # Redirecionamento para evitar o reenvio do formulário no F5
        return redirect(url_for('routes.update_task', task_id=task_id))

    return render_template("updateTasks.html", task=tarefa)

@routes.route('/delete-task/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    from crud import excluir_tarefa
    excluir_tarefa(task_id)
    return redirect(url_for('routes.home'))
