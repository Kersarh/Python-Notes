# POETRY

Страница документации
<https://poetry.eustace.io/docs/>

## Установка

`pip install poetry`

## Проверить настройки

`poetry config --list`

## Для сохранения venv в папке проекта

`poetry config settings.virtualenvs.in-project true`

## файл pyproject.toml в интерактивном режиме

`poetry init`

## Создать проект

`poetry new poetry-demo`

## установить пакет

`poetry add pyqt5`

## Установка всех зависимостей из poetry.lock

`poetry install`

## Подготовка пакета к публикации

Эта команда упакует вашу библиотеку в два разных формата:
исходники и wheel, который является скомпилированным пакетом.  
`poetry build`

## Публикация

`poetry publish`

## Для публикации в частный репозиторий

`poetry publish -r my-repository`

## Добавить репозиторий

Это установит URL-адрес для хранилища foo на `https://foo.bar/simple/`.
`poetry config repositories.foo https://foo.bar/simple/`

## Если вы хотите сохранить свои учетные данные для определенного репозитория

`poetry config http-basic.foo username password`
