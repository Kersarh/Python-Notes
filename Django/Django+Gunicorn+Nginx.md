# Django + gunicorn + nginx

## Установка

```bash
apt install python3
apt install libpq-dev python3-dev
apt install python3-pip
apt install nginx
apt install nano
apt install postgresql postgresql-contrib

pip3 install django
pip3 install gunicorn

# опционально
pip install django-crispy-forms
pip install psycopg2
```

### Создаем проект или переносим готовый

```bash
django-admin.py startproject mySite
```
не забываем про collectstatic перед выкладкой, чтобы nginx мог ее корректно подгружать.
```bash
python3 manage.py collectstatic
```
Проект лучше создавать c использованием виртуального окружения.

### Проверяем gunicorn

Из папки проекта там где лежит manage.py запускаем gunicorn указав Ваш IP
```bash
gunicorn mySite.wsgi:application --bind 111.111.111.111:8000
```

При этом сайт будет отображаться без статических файлов это нормально!

Иногда gunicorn может оставаться в памяти
```bash
killall gunicorn
```

### Создадим конфиг файл для gunicorn

```bash
cd /opt/mySite/mySite/` # каталог с settings.py
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
        root /opt/mySite/;  # где manage.py
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
touch mySite.service
nano mySite.service
```
Содержимое файла:
```
[Unit]
Description=mySite
After=nginx.service

[Service]
Type=forking
WorkingDirectory=/opt/mySite/ # где manage.py
ExecStart=/opt/mySite/env/bin/gunicorn mySite.wsgi:application -c /opt/mySite/mySite/gunicorn.conf.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Проверяем статус и подключаем его и запускаем:

```bash
systemctl status mySite.service
systemctl enable mySite.service
systemctl start mySite.service
```



## Автозапуск - Supervisor

Чтобы наше приложение стартовало после сбоя.
```bash
apt install supervisor
```
создадим конфиг супервизора и отредактируем его
```bash
cd /etc/supervisor/conf.d/
touch mySite.conf
nano mySite.conf
```

Пишем наш конфиг
```text
[program:myproject]
command=/opt/mySite/env/bin/gunicorn mySite.wsgi:application -c /opt/mySite/mySite/gunicorn.conf.py
directory=/opt/mySite/myproject
user=nobody
autorestart=true
redirect_stderr=true
```

Команды для supervisor

```bash
supervisorctl reread
supervisorctl update
supervisorctl status mySite
supervisorctl restart mySite
```
