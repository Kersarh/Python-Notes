# PyLint

## Установка
`pip install pylint`

Если не работает в Windows
Вводим в консоль
```
chcp 65001 && pip install pylint
run chcp 65001
pip install pylint
```

Или одной строкой  
`chcp 65001 && pip install pylint && chcp 866 && pip install pylint`  
__________
Cоздать файл конфигурации в корне проекта:  
`pylint --generate-rcfile > .pylintrc`
__________
