# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido actual del directorio al contenedor en /app
COPY . /app

# Comando por defecto para ejecutar tu aplicación
CMD ["python", "app.py"]
