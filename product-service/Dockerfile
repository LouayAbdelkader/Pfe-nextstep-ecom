# Utiliser une image de base Python basée sur Alpine
FROM python:3.12-alpine

# Définir le répertoire de travail
WORKDIR /app

# Mettre à jour les paquets système d'Alpine pour s'assurer que zlib est à jour
RUN apk update && apk upgrade

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY . .

# Installer les dépendances Python
# Note : build-base est l'équivalent de build-essential pour compiler des dépendances si nécessaire
RUN apk add --no-cache build-base \
    && pip install --no-cache-dir --upgrade pip setuptools \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del build-base

# Exposer le port utilisé par Flask
EXPOSE 5001

# Commande pour démarrer l'application
CMD ["python", "main.py"]
