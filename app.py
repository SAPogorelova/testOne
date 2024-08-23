#импортируем необходимые элементы из библиотеки Flask:
#Flask — основной класс приложения Flask.
#request — объект, содержающий данные о текущем HTTP-запросе.
#jsonify — функция для создания ответа в формате JSON.
#abort — функция для прерывания выполнения и возвращения HTTP-ошибок.

from flask import Flask, request, jsonify, abort

#создаем экземпляр приложения Flask. __name__ указывает Flask, где искать ресурсы, такие как HTML-шаблоны
#и файлы
app = Flask(__name__)

#создание словаря
users = {}

#1. Добавить пользователя
@app.route("/users", methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get('id')
    username = data.get('username')

    #Проверяем, существует ли уже пользователь с таким user_id или username. Если да, возвращаем ошибку 400.
    #Если нет, добавляем пользователя в словарь и возвращаем сообщение об успехе с кодом 201.

    if user_id in users or username in users.values():
        abort(400, description="Пользователь уже существует.")

    users[user_id] = username
    return jsonify({"message": "Пользователь добавлен."}), 201 #HTTP-код состояния 201 означает "Created" (англ. "Создано").

#2. получить пользователей
@app.route('/users', methods=['GET'])
def get_users():
    limit = request.args.get('limit', default=10, type=int) # извлекаем параметр limit из строки запроса (request.args). Возвращается список имен пользователей, ограниченный указанным limit. По умолчанию выводится до 10 пользователей.
    usernames = list(users.values())
    return jsonify(usernames[:limit]), 200 #HTTP-код состояния 200 означает "OK" (рус. "ОК")

#3. обновить username
@app.route('/users', methods=['PATCH'])
def update_users():
    data = request.get_json()
    user_id = data.get('id')
    username = data.get('username')

    # Если пользователь не существует, создаем нового
    if user_id not in users:
        users[user_id] = username
        return jsonify({"message": "Пользователь создан."}), 201  #HTTP-код состояния 201 означает "Created" (англ. "Создано").

    # Если пользователь существует, он обновляется. Выводится соответствующее сообщение
    users[user_id] = username
    return jsonify({"message": "Пользователь обновлен."}), 200  #HTTP-код состояния 200 означает "OK" (рус. "ОК")



#4. удаление. Проверяем, существует ли пользователь с данным user_id. Если нет, генерируем ошибку 404.
              #Если пользователь существует, удаляем его из словаря и возвращаем сообщение об успехе.
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        abort(404, description="Пользователь не найден.")   #Код состояния HTTP 404 означает "Не найдено" (англ. "Not Found")

    del users[user_id]
    return jsonify({"message": "Пользователь удален."}), 204   #Код состояния HTTP 204 означает "No Content" (англ. "Нет содержимого").

# 5. Получение пользователя по id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    if user_id not in users:
        abort(404, description="Пользователь не найден.") #Код состояния HTTP 404 означает "Не найдено" (англ. "Not Found")


    return jsonify({"id": user_id, "username": users[user_id]}), 200  #HTTP-код состояния 200 означает "OK" (рус. "ОК")


if __name__ == "__main__":
    app.run("0.0.0.0", 8000, debug=True)
