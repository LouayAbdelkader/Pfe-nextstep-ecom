# Utiliser une image de base Python plus récente avec moins de vulnérabilités
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Mettre à jour les paquets système pour corriger perl-base et zlib1g
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt requirements.txt
COPY . .

# Installer les dépendances Python avec les versions corrigées
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Exposer le port que l'application Flask va utiliser
EXPOSE 5001

# Commande pour démarrer l'application Flask
CMD ["python", "main.py"]
