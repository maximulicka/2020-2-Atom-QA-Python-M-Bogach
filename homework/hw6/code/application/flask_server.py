import threading
from flask import Flask, request, jsonify, make_response
import settings
import requests
import json

app = Flask(__name__)
DATA = {}


# Напишем функцию, которая будет отвечать за запуск нашего приложения
def run_app():
    # Используем треды, чтобы была общая память с pytest
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.APP_HOST,
        'port': settings.APP_PORT
    })

    server.start()
    return server


# Добавляем точку завершения приложения, чтобы мы могли его при необходимостм правильно закрыть
def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_app()


@app.route('/', methods=['POST'])
def socket_client_method():
    if request.method == 'POST':
        return jsonify(json.loads(request.data.decode()), 200)


@app.route('/task_list', methods=['POST', 'PUT'])
def task_list_req():
    headers = dict(request.headers.items())
    data = json.loads(request.data)
    response = requests.post('http://127.0.0.1:1052', headers=headers, data=json.dumps(data))
    return make_response((jsonify({'msg': response.text})), response.status_code)


@app.route('/server_error', methods=['POST', 'PUT'])
def task_server_error():
    headers = request.headers
    data = json.loads(request.data)
    response = requests.post('http://127.0.0.1:1052', headers=headers, data=json.dumps(data))
    return make_response((jsonify({'msg': response.text})), response.status_code)


@app.route('/new', methods=['POST', 'PUT'])
def task_new():
    headers = request.headers
    data = json.loads(request.data)
    response = requests.post('http://127.0.0.1:1052', headers=headers, data=json.dumps(data))
    return make_response((jsonify({'msg': response.text})), response.status_code)


if __name__ == '__main__':
    run_app()
