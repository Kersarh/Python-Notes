1. Установим cython
```bash
pip install Cython
```

###Linux
2. Конвертируем python-скрипт в Си:
```bash
cython -3 example.py
```

3. Компилируем полученный Си-файл:
```bash
gcc -pthread -Wno-unused-result -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/usr/local/include/python3.3m -c example.c -o example.o
```
Получаем объектный файл example.о
Осталось слинковать его в бинарник.

4. линковка в бинарник
```bash
link = gcc -pthread -shared example.o -o example.so
```

###Windows

pyd 32bit
```bash
cython -o example.c example.py
gcc -c -Ofast -IC:\Python35-32\include -o example.o example.c
gcc -shared -LC:\Python35-32\libs -o example.pyd example.o -lpython35
```

pyd 64bit
```bash
cython -o example.c example.py
gcc -c -DMS_WIN64 -Ofast -IC:\Python35\include -o example.o example.c
gcc -shared -LC:\Python35\libs -o example.pyd example.o -lpython35
```

exe 64bit
```bash
cython --embed -o example.c example.py
gcc -municode -DMS_WIN64 -mthreads -Wall -O -IC:\Python35\include -LC:\Python35\libs example.c -lpython35 -o example.exe
```
