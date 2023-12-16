from flask import Blueprint

esp32 = Blueprint('esp32', __name__)

@esp32.route('/data', methods=['POST'])
def receive_data():
    # Lógica para manejar los datos del ESP32
    return "Datos recibidos"
