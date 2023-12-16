class ESP32Data:
    def __init__(self, numero, mensaje):
        self.numero = numero
        self.mensaje = mensaje

    def __repr__(self):
        return f'<ESP32Data numero={self.numero} mensaje={self.mensaje}>'
