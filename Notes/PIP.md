# PIP

## Обновить PIP

`python -m pip install --upgrade pip`

## Устаревшие пакеты

`pip list --outdated`

## Создать файл зависимостей в текущем каталоге

`pip freeze > requirements.txt`

## Установка зависимостей из файла

`pip install -r requirements.txt`

## Upgrade зависимостей из файла requirements.txt

`pip install --upgrade -r requirements.txt`

## Upgrade всех для win в командной строке

`for /F "delims===" %i in ('pip freeze -l') do pip install -U %i`

