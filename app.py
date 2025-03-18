from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    tasks = [{"id": 1, "title": "Estudar Flask"}, {"id": 2, "title": "Criar projeto To-Do"}]
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
