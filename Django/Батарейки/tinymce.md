# django-tinymce

## Установка

```pip install django-tinymce```

В `settings.py` добавить:  
```python
INSTALLED_APPS = [
    ...
    'tinymce',
]
```

В `urls.py` добавить:  
```python
urlpatterns = [
    ...
    re_path(r'^tinymce/', include('tinymce.urls')),
]
```

В `models.py` добавить:  

```python
from tinymce.models import HTMLField
...
content = HTMLField()  # поле для которого будет работать tinymce (в место TextField())
...
```

## Настройки

По желанию в `settings.py` добавить:

```python
TINYMCE_DEFAULT_CONFIG={
    'theme' : "advanced",
    'plugins': "table,spellchecker,paste,searchreplace",
    'forced_root_block' : '', # отключаем добавление тега <p>
    }
```

## Выполнить  

`manage.py collectstatic`

Все можно пользоваться!
