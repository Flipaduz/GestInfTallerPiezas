from flask import Flask
from backend.routes.piezas import piezas_bp

app = Flask(__name__)
app.register_blueprint(piezas_bp)

if __name__ == '__main__':
    app.run(debug=True)