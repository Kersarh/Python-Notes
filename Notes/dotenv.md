# Dotenv - хранилище переменных окружения

## Установка

`pip install -U python-dotenv`

## Использование

Примерная структура папок в проекте

```
.
├── .env
└── settings.py
```

#### .env

Файл содержит переменные окружения 

```
# Список
PASSWORD=password123
KEY=qwerty123
```

Подключаем в файле `settings.py`:

```
# settings.py
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)
```

Получаем значение из переменных окружения

```
# settings.py
import os
SECRET_KEY = os.getenv("KEY")
DATABASE_PASSWORD = os.getenv("PASSWORD")
```

