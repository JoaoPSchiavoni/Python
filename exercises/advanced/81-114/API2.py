'''API - É um lugar para disponibilizar recursos e/ou funcionalidades
1. Objetivo - Criar uma API que disponibiliza a consulta, criacao, edicao e exclusao de livros.
2. URL base - localhost
3. Endpoints
    - localhost/livros (GET)
    - localhost/livros/{id} (GET)
    - localhost/livros (POST)
    - localhost/livros/{id} (PUT)
    - localhost/livros (DELETE)
4. Quais recursos - Livros'''
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis',
        'autor': 'J.R.R. Tolkien',
    },
    {
        'id': 2,
        'titulo': '1984',
        'autor': 'George Orwell',
    },
    {
        'id': 3,
        'titulo': 'O Hobbit',
        'autor': 'J.R.R. Tolkien',
    },
    {
        'id': 4,
        'titulo': 'Dom Casmurro',
        'autor': 'Machado de Assis',
    },
    {
        'id': 5,
        'titulo': 'A Revolução dos Bichos',
        'autor': 'George Orwell',
    },
    {
        'id': 6,
        'titulo': 'O Pequeno Príncipe',
        'autor': 'Antoine de Saint-Exupéry',
    },
    {
        'id': 7,
        'titulo': 'A Metamorfose',
        'autor': 'Franz Kafka',
    },
    {
        'id': 8,
        'titulo': 'Crime e Castigo',
        'autor': 'Fiódor Dostoiévski',
    },
    {
        'id': 9,
        'titulo': 'A menina que roubava livros',
        'autor': 'Markus Zusak'
    },
    {
        'id': 10,
        'titulo': 'Mein Kampf I',
        'autor': 'Adolf Hitler'
    },
    {
         'id': 10,
        'titulo': 'Mein Kampf II',
        'autor': 'Adolf Hitler'
    }
]

#consultar todos
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
if __name__ == '__main__':
    app.run(port=5123, host='localhost', debug=True)

# http://127.0.0.1:5000/livros
