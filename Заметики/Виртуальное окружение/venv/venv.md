# Заметка по включению и использованию VENV

## Создание

Создаем папку с проектом `my_project`и перейдем в нее.  
Создаем виртуальное окружение под именем `my_venv`.  
```python -m venv my_venv```

Запустим виртуальное окружение, выполнив:  
```my_venv\Scripts\activate```  
или  
```my_venv\Scripts\activate.bat```  
  
Должна появится приписка в командной строке  
`(myvenv) C:\my_project>`  
  
## Авто использование в скрипте  

Добавить первой строкой в скрипт  
```#! C:\Projects\my_venv\Scripts\python.exe```  
или  
```#! my_venv\Scripts\python.exe```  
