from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

added_item = []

# Определение маршрута (endpoint)
@app.route('/')
def hello_world():
    """
    Это простой эндпоинт, который возвращает "Привет, мир!"
    ---
    responses:
      200:
        description: Приветствие
    """
    return f'Привет, мир! Added item: {added_item}'

@app.route('/test/<int:item_id>')
def read_item(item_id):
    """
    Этот эндпоинт возвращает JSON с информацией о элементе
    ---
    parameters:
      - name: item_id
        in: path
        type: int
        description: ID элемента
    responses:
      200:
        description: Информация о элементе
        schema:
          type: object
          properties:
            item:
              type: int
    """
    return {"item": item_id}

@app.route('/test2/<int:item_id>', methods=['POST'])
def add_item(item_id):
    """
    Этот эндпоинт возвращает JSON с информацией о элементе
    ---
    parameters:
      - name: item_id
        in: path
        type: int
        description: ID элемента
    responses:
      200:
        description: Информация о элементе
        schema:
          type: object
          properties:
            item:
              type: int
    """
    global added_item
    added_item.append(item_id)
    return {"added": item_id}

if __name__ == '__main__':
    # host для Docker
    app.run(host='0.0.0.0', port=5000)
