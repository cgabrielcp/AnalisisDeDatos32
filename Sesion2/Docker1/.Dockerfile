# Definir Imagen Base
FROM python:3.9-slim

# Instalaciones de sistemas y actualizaciones
RUN pip3 install --upgrade pip && \
    pip3 install notebook==6.5.6

#Se define el directorio.
WORKDIR /workspace 

# Donde almacenar mis archivos de configuracion
RUN mkdir -p /root/.jupyter

# Ingresar las variables 
RUN echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.allow_root = True" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /root/.jupyter/jupyter_notebook_config.py
