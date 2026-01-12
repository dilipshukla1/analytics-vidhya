# frontend/Dockerfile

FROM nginx:alpine

# Copy frontend HTML/JS files
COPY . /usr/share/nginx/html

# Overwrite default nginx.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

