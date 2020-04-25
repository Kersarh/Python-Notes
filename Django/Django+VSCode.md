# Django + VS Code

## Установка pylint

Устанавливаем pylint и pylint-django

```bash
pip install pylint
pip install pylint-django
```

## Настройки VS code

В файле `settings.json`

```json
"python.linting.pylintArgs": [
        "--load-plugins",
        "pylint_django"
    ],
```

