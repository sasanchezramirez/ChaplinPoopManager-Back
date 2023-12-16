from flask import Blueprint,  request, jsonify
from models.data_model import ESP32Data

esp32 = Blueprint('esp32', __name__)

@esp32.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    esp32_data = ESP32Data(numero=data['numero'], mensaje=data['mensaje'])
    print(esp32_data)  # Imprime los valores para verificar
    return jsonify({'status': 'Datos recibidos'}), 200
