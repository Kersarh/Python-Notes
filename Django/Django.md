# Django

## Установка

`pip install django`

Для работы с postgresql понадобится

`apt build-dep python-psycopg2`

## Создать проект

`django-admin startproject project_name`

## Создать приложение

`python manage.py startapp app_name` 
или просто    
`manage.py startapp app_name`

## Запустить сервер

`manage.py runserver`

## Создать админа

`manage.py migrate`  
`manage.py createsuperuser`

## Миграция если в базу есть данные

`manage.py migrate --fake-initial`

## Сбор статических файлов

`manage.py collectstatic`  
Проходит по `STATICFILES_DIRS` и `STATICFILES_FINDERS` и копирует все статичные файлы из папок static приложений в заданную вами в STATIC_ROOT директорию.  
Это позволяет разрешать ресурсы в виде статичных данных с помощью той же логики, что и у Django-сервера в режиме разработки, и собирать в одном месте для  веб-сервера все статичные файлы.

