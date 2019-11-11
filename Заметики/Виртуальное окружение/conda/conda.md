# conda в составе Anaconda или Miniconda

## Команды

```bash
    conda search package_name — поиск пакета через conda  
    conda install package_name — установка пакета через conda  
    conda install — установка всего стандартного набора пакетов — более 150, около 3 Гб  
    conda list — список установленных пакетов  
    conda update conda — обновление conda  
    conda update --all — обновление всего возможного  
    conda clean -t — удаление кеша — архивов .tar.bz2, которые могут занимать много места и не нужны  
```

## Cоздать виртуальное окружение

`conda create -p C:\ENV_FOLDER --copy --yes python=3.7.2 conda`
