# Servicer 
server {
    listen 80;
    server_name 35.78.195.204;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/mghtay/app;
    }
    location /media/ {
        root /home/mghtay/app;
    }

    location / {
        include /home/mghtay/app/uwsgi_params;
        proxy_pass http://unix:/run/gunicorn.sock;

        proxy_pass_header X-CSRFToken;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto http;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header HOST $http_host;
        proxy_set_header X-NginX-Proxy true;
    }
}

# uwsgi_params
uwsgi_param QUERY_STRING $query_string;
uwsgi_param REQUEST_METHOD $request_method;
uwsgi_param CONTENT_TYPE $content_type;
uwsgi_param CONTENT_LENGTH $content_length;

uwsgi_param REQUEST_URI $request_uri;
uwsgi_param PATH_INFO $document_uri;
uwsgi_param DOCUMENT_ROOT $document_root;
uwsgi_param SERVER_PROTOCOL $server_protocol;
uwsgi_param REQUEST_SCHEME $scheme;
uwsgi_param HTTPS $https if_not_empty;

uwsgi_param REMOTE_ADDR $remote_addr;
uwsgi_param REMOTE_PORT $remote_port;
uwsgi_param SERVER_PORT $server_port;
uwsgi_param SERVER_NAME $server_name;


# http://54.238.109.35/
