# Django + gunicorn + nginx

## Установка

```bash
apt install python3
apt install python3-pip
apt install nginx
apt install nano
pip3 install django
pip3 install gunicorn
```

### Создаем наш проект

```bash
django-admin.py startproject myproject
```
не забываем про collectstatic перед выкладкой, чтобы nginx мог ее корректно подгружать.
```bash
python3 manage.py collectstatic
```
Проект лучше создавать в виртуальном окружении.

### Проверяем gunicorn

Из папки проекта там где лежит manage.py запускаем gunicorn указав Ваш IP
```bash
gunicorn myproject.wsgi:application --bind 111.111.111.111:8000
```

При этом сайт будет отображаться без статических файлов это нормально!

Иногда gunicorn может оставаться в памяти
```bash
killall gunicorn
```

### Создадим конфиг файл для gunicorn

```bash
cd /opt/my_site/myproject/myproject` # каталог с settings.py
touch gunicorn.conf.py
```
Открываем
```bash
nano gunicorn.conf.py
```
Пишем
```text
bind = '127.0.0.1:8000'
workers = 3
user = "nobody"
```
## Настроим nginx

Перейдем в /etc/nginx/sites-available/
```bash
cd /etc/nginx/sites-available/
```
и откроем default
```bash
nano default
```

Удаляем оттуда все и пишем

```nginx
server {
    listen 80;
    server_name 111.111.111.111; # ip или доменное имя
    access_log  /var/log/nginx/site.log;

    location /static/ {
        root /opt/my_site/myproject/;  # где manage.py
        expires 30d;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }
```

Сохраняем, выходим, перезапускам nginx
```bash
service nginx restart
```
Если все правильно переходим в браузере по адресу сайта и радуемся итогу.

## Автозапуск - systemd
Создадим и отредактируем файл настроек systemd
создадим конфиг и отредактируем его

```bash
cd /etc/systemd/system/
touch myproject.service
nano myproject.conf
```
Содержимое файла:
```
[Unit]
Description=My_Project
After=nginx.service

[Service]
Type=forking
ExecStart=/opt/my_site/env/bin/gunicorn myproject.wsgi:application -c /opt/my_site/myproject/myproject/gunicorn.conf.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Проверяем статус и подключаем его и запускаем:

```bash
systemctl status myproject
systemctl enable myproject
systemctl start myproject
```



## Автозапуск - Supervisor

Чтобы наше приложение стартовало после сбоя.
```bash
apt install supervisor
```
создадим конфиг супервизора и отредактируем его
```bash
cd /etc/supervisor/conf.d/
touch myproject.conf
nano myproject.conf
```

Пишем наш конфиг
```text
[program:myproject]
command=/opt/my_site/env/bin/gunicorn myproject.wsgi:application -c /opt/my_site/myproject/myproject/gunicorn.conf.py
directory=/opt/my_site/myproject
user=nobody
autorestart=true
redirect_stderr=true
```

### Команды для supervisor

```bash
supervisorctl reread
supervisorctl update
supervisorctl status myproject
supervisorctl restart myproject
```