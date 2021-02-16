# Заметка по включению и использованию VENV

## Создание

Создаем папку с проектом `my_project`и перейдем в нее.  
Создаем виртуальное окружение под именем `my_venv`.  
```python -m venv my_venv```

Запустим виртуальное окружение, выполнив:  
```my_venv\Scripts\activate```  
или  
```my_venv\Scripts\activate.bat```  

для **Linux**

`source env/bin/activate`

Должна появится приписка в командной строке  
`(my_venv) C:\my_project>`  

## Авто использование в скрипте  

Добавить первой строкой в скрипт  
```#! C:\Projects\my_venv\Scripts\python.exe```  
или  
```#! my_venv\Scripts\python.exe```  
