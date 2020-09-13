## Использование embedded Python

#### Загрузка

Идем на python.org и скачиваем нужную версию python embedded.
Вся установка сводится к простой распаковке архива.

#### Установка PIP (Опционально)
Если необходима установка модулей может потребоваться установить pip.

Для этого в файле python37._pth нужно раскомментировать строку:
```python
import site
```

Скачиваем pip. 

Через curl:

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Или из браузера

```
https://bootstrap.pypa.io/get-pip.py
```

Переходим в папку с embedded Python и устанавливаем pip:

```
python get-pip.py
```

Проверяем работоспособность 

```
Scripts\pip.exe -V
```

#### Использование

Запускаем наш скрипт командой

```
[путь к python.exe] MyScript.py
```