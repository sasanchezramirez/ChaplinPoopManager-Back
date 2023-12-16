from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def welcome():
    return "Bienvenido al Backend del ESP32"
