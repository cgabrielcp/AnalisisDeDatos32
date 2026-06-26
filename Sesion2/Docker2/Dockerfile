# Escoger una imagen base
FROM python:3.9-slim 

# Definir nuestro directorio de trabajo
WORKDIR /app

# Copiamos las librerias para instalar
COPY requirements.txt ./

# Instalamos las librerias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el contenido en el directorio de trabajo
COPY . .

# exponer el puerto del contenedor
EXPOSE 5000

# Comando de ejecucion
CMD [ "python", "app.py" ]