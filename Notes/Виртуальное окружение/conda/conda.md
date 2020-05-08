# Conda в составе Anaconda или Miniconda

## Команды

```bash
    conda info - информация о текущей версии 
    conda search package_name — поиск пакета через conda  
    conda install package_name — установка пакета через conda  
    conda install — установка ВСЕГО стандартного набора пакетов
    conda remove package_name - Удалить пакет из активной среды
    conda list — список установленных пакетов  
    conda update conda — обновление conda
    conda update anaconda - обновление anaconda
    conda update --all — обновление всего возможного  
    conda clean -t — удаление кеша — архивов .tar.bz2, которые могут занимать много места и не нужны  
```

## Создать виртуальное окружение

`conda create -p C:\ENV_FOLDER --copy --yes python=3.7.2 conda`

## Создать requirements.txt

`conda list -e > requirements.txt`

## Запуск и остановка



### Доп команды

```
conda info --envs - Получить список всех моих окружений. Активная среда показана с *
conda env export > puppies.yml - Сохранить текущую среду в файл
conda env create -f puppies.yml - Загрузить среду из файла
conda search --full-name python - версии Python, доступные для установки

```

