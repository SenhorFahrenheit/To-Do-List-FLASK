from flask import Flask
from routes.routes import routes  # Importando as rotas

app = Flask(__name__)

# Registrando o Blueprint das rotas
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
