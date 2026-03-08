# Use official Nginx image based on Alpine Linux for a lightweight container
FROM nginx:alpine

# Copy custom HTML file to the default Nginx web root directory
COPY index.html /usr/share/nginx/html/

# Copy custom Nginx configuration file to override the default configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 to allow external HTTP traffic
EXPOSE 80