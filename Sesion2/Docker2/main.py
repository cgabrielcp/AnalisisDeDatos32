
from flask import Flask
from flasgger import Swagger

# Crear una instania de la clase Flask y con el nombre del modulo name
app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'Mi API',
    'uiversion': 3
}
 
swagger = Swagger(app)

# Ruta 1
@app.route('/api/hello')
def hello():
    """
        Get Hello

        Retorna mensaje de conexion
    """
    return 'Hola Mundo desde Docker'

# Ruta 1
@app.route('/api/getData')
def getData():
    """
        Get Hello

        Retorna mensaje de conexion
    """
    resultado = "Data Obtenida"

    return resultado


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



