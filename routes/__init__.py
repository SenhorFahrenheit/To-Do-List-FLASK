from flask import Blueprint

# Criando um Blueprint para as rotas
routes = Blueprint('routes', __name__)

# Importando o arquivo routes.py para registrar as rotas
from .routes import *
