from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registro de rutas
    from .routes.esp32_routes import esp32
    app.register_blueprint(esp32)

    from.routes.main_routes import main
    app.register_blueprint(main)

    return app
