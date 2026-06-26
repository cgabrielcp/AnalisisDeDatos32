
from flask import Flask

# Crear una instania de la clase Flask y con el nombre del modulo name
app = Flask(__name__)

# Ruta 1
@app.route('/api/hello')
def hello():
    """
        Get Hello

        Retorna mensaje de conexion
    """
    return 'Hola Mundo desde Docker'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



