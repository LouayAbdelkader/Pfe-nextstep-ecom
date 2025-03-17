# Utiliser une image Nginx légère avec une version spécifique et mise à jour
FROM nginx:1.27.2-alpine

# Mettre à jour les dépendances pour corriger les vulnérabilités
RUN apk update && apk upgrade --no-cache \
    && rm -rf /var/cache/apk/*  # Nettoyer le cache pour réduire la taille

# Supprimer la configuration Nginx par défaut
RUN rm -rf /usr/share/nginx/html/*

# Copier les fichiers HTML, CSS, et JS vers Nginx
COPY . /usr/share/nginx/html

# S'assurer que les permissions sont correctes
RUN chown -R nginx:nginx /usr/share/nginx/html \
    && chmod -R 755 /usr/share/nginx/html

# Exposer le port 80
EXPOSE 80

# Lancer Nginx
CMD ["nginx", "-g", "daemon off;"]
