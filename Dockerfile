# Usa la imagen base de Python
FROM python:3.6

# Configura el directorio de trabajo
WORKDIR /app

# Copia el código fuente al contenedor
COPY . .

# Instala las dependencias
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en_core_web_sm

# Expone el puerto que utilizará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python3", "main.py"]
