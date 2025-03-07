# Utiliser une image Nginx légère
FROM nginx:alpine

# Supprimer la configuration Nginx par défaut
RUN rm -rf /usr/share/nginx/html/*

# Copier les fichiers HTML, CSS, et JS vers Nginx
COPY . /usr/share/nginx/html

# Exposer le port 80
EXPOSE 80

# Lancer Nginx
CMD ["nginx", "-g", "daemon off;"]
