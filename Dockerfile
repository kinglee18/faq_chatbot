# Usa la imagen base de Python
FROM python:3.6

# Configura el directorio de trabajo
WORKDIR /app

# Copia el código fuente al contenedor
COPY . .

# Instala las dependencias
RUN pip3 install -r requirements.txt

# Expone el puerto que utilizará la aplicación
EXPOSE 8080
EXPOSE 5000
ENV PORT 8080
ENV HOST 0.0.0.0

# Comando para ejecutar la aplicación
CMD ["python3", "main.py"]
