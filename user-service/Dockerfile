# Utiliser une image de base Python plus récente
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Mettre à jour les paquets système et installer les outils nécessaires
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y build-essential wget \
    && apt-get clean

# Compiler une version corrigée de zlib
RUN wget https://zlib.net/zlib-1.3.1.tar.gz \
    && tar -xzf zlib-1.3.1.tar.gz \
    && cd zlib-1.3.1 \
    && ./configure && make && make install \
    && ldconfig \
    && cd .. && rm -rf zlib-1.3.1* \
    && apt-get purge -y build-essential wget && apt-get autoremove -y

# Tenter de supprimer perl-base si non nécessaire
RUN apt-get remove -y perl-base && apt-get autoremove -y || true

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY . .

# Mettre à jour pip et installer les dépendances Python
RUN pip install --no-cache-dir --upgrade pip setuptools \
    && pip install --no-cache-dir -r requirements.txt

# Exposer le port utilisé par Flask
EXPOSE 5001

# Commande pour démarrer l'application
CMD ["python", "main.py"]
