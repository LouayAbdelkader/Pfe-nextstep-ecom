# Utiliser une image de base Python sécurisée
FROM python:3.12-alpine

# Définir le répertoire de travail
WORKDIR /app

# Ajouter un utilisateur non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Mettre à jour les paquets et installer les dépendances
RUN apk update && apk upgrade

# Ajouter un fichier .dockerignore
RUN echo "\n.env\n.git\n__pycache__/\n*.pyc\n*.pyo\nnode_modules/\n" > .dockerignore

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY . .

# Installer les dépendances Python
RUN apk add --no-cache build-base \
    && pip install --no-cache-dir --upgrade pip setuptools \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del build-base

# Exposer le port utilisé par Flask
EXPOSE 5001

# Commande pour démarrer l'application
CMD ["python", "main.py"]
