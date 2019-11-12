# django-cleanup

При удалении файлов и картинок из админ панели django он оставляет их в файловой системе.  
Для удаления лишних данных нужно установить библиотеку django-cleanup.  

## Установка

`pip install django-cleanup`

в файле `settings.py` подключаем.

```python
INSTALLED_APPS = (
    ...
    'django_cleanup',
)
```

Теперь при удалении поста буду автоматически удаляться и файлы из папки media.

## Репозиторий

<https://github.com/un1t/django-cleanup>  
