### Установка PyInstaller

В командной строке:

`pip install pyinstaller`

### Создание spec-файла (файла спецификации)

Pyinstaller создает приложение, выполняя содержимое файла спецификации.

Чтобы создать spec-файл, через командную строку в папке с проектом набираем:

`pyi-makespec --onefile main.py`

Флаг `--onefile` создает файл спецификации, который позволит упаковать всё необходимое в один exe-файл.

### Создание exe

В командной строке вводим:

`pyinstaller mygame.spec`

### Без spec файла
Предварительное создание spec не является обызательным. воздно запускать программу указывая основной файл программы.
`pyinstaller -F -w -i( to set up icon on your .exe) main.py`

`-F`,`--onefile` – все будет упаковано в единый исполняемый файл.

`-w` – блокирует создание консольного окна, если же ваше приложение консольное, вам этот флаг использовать **не нужно**. 

`-i` – установка иконки на наш исполняемый файл, после флага нужно указать полный путь к иконке с указанием её имени.

`--upx-dir=DIR_TO_upx.exe` - Сжатие

