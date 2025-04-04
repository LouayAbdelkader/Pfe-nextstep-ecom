# Utiliser une image de base Python sécurisée
FROM python:3.12-alpine

# Définir le répertoire de travail
WORKDIR /app

# Ajouter un utilisateur non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# ⛔️ On ne peut pas exécuter apk update en tant qu'utilisateur non-root
# ✅ Faire les installations système AVANT de passer à appuser
RUN apk update && apk upgrade --no-cache \
    && apk add --no-cache build-base

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir --upgrade pip setuptools \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del build-base

# Ajouter un fichier .dockerignore (⚠️ Ceci ne sert à rien dans un Dockerfile)
# Le .dockerignore doit exister **dans votre projet local**, pas dans le Dockerfile.
# Donc cette ligne peut être supprimée:
# RUN echo "\n.env\n.git\n__pycache__/\n*.pyc\n*.pyo\nnode_modules/\n" > .dockerignore

# Donner les droits à appuser si nécessaire
RUN chown -R appuser:appgroup /app

# Passer à l'utilisateur non-root
USER appuser

# Exposer le port utilisé par Flask
EXPOSE 5001

# Commande pour démarrer l'application
CMD ["python", "main.py"]
