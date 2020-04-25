# Отправка e-mail

## **settings.py** 

в зависимости от хостинга почты

**mail.ru**
```python
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = "your@mail.ru"
EMAIL_HOST_PASSWORD = "password"
EMAIL_USE_TLS = True
```
**gmail.com**
```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "your@gmail.com"
EMAIL_HOST_PASSWORD = "password"
EMAIL_USE_TLS = True
```
**yandex.ru**

```python
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "your@yandex.ru"
EMAIL_HOST_PASSWORD = "password"
EMAIL_USE_SSL = True
```

**Отправка сообщений об ошибках**

```python
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```



## Отправить сообщение

Чтобы отправить письмо нужно в коде вызвать команду send_mail

```python
from django.conf import settings
send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, ['to@example.com'])
```



Добавить имя отправителя (или название), то используйте `headers`:

```python
headers = {'To': '{} <{}>'.format(user.get_full_name(), user.email)}
send_mail('Тема', 'Тело письма' , settings.EMAIL_HOST_USER, ['to@example.com'], headers=headers)
```

Если вы хотите использовать html-теги в теле письма, то удобно создать отдельный файл и использовать `render_to_string()`:

```python
from django.conf import settings
msg = render_to_string('path\to\template.html', {'test_variable': 'xxx'})
send_mail('Тема', msg , settings.EMAIL_HOST_USER, ['to@example.com'])
```