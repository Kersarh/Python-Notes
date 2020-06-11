Подробное описание 
https://docs.python.org/3/using/windows.html

#### Для получения ПОЛНОЙ OFF-Line версии

```bash
python-3.8.3.exe /layout
```
#### Установка аргументы командной строки

`/quiet` - полностью скрыть пользовательский интерфейс и установить Python
без вывода сообщений.

`/passive` - пропустить взаимодействие с пользователем,
но по-прежнему отображать прогресс и ошибки.

`/uninstall` - для немедленного начала удаления Python
приглашение не будет отображаться.

Примеры
```bash
python-3.8.3.exe /quiet InstallAllUsers=1 PrependPath=1 TargetDir=c:\Python\Python3
```
```bash
python-3.8.3.exe /passive InstallAllUsers=1 PrependPath=1 TargetDir=c:\Python\Python3
```

`PrependPath `- добавляет каталоги install и Scripts в PATH и .PY в PATHEXT

