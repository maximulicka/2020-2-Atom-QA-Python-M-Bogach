from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import json


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'max': generate_password_hash('111'),
    'julia': generate_password_hash('222'),
    'boris': generate_password_hash('333')
}

teams = {
    'max': {
        'name': 'Barcelona',
        'Country': 'Spain',
        'Stadium': 'Camp Now',
        'price_team': '1 billion $'
        },
    'julia': {
        'name': 'Arsenal',
        'Country': 'England',
        'Stadium': 'Camp Now',
        'price_team': '800 million $'
    },
    'boris': {
        'name': 'CSKA',
        'Country': 'Russia',
        'Stadium': 'VEB-Arena',
        'price_team': '100 million $'
    }
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


@app.route("/")
@auth.login_required
def index():
    return f'Hello, {auth.current_user()}'


@app.route("/profile")
@auth.login_required
def profile():
    return f'{auth.current_user()}, this your profile'


@app.route("/message")
@auth.login_required
def message():
    return f'{auth.current_user()}, you have new message!'


@app.route("/sport_team")
@auth.login_required
def sport_team():
    return jsonify(teams)


@app.route("/logout")
@auth.login_required
def logout():
    return f'{auth.current_user()}, was logout', 401


@app.route("/sport_team", methods=['POST'])
def post_method():
    if request.method == 'POST':
        data = json.loads(request.data)
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5555)
