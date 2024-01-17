# Utilisez une image de base Python
FROM python:3.9-slim

# Définissez un répertoire de travail
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY requirements.txt .

# Installez les dépendances avec pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Copiez le reste de votre application
COPY . .

# Commande pour démarrer votre application
CMD ["python", "app.py"]
