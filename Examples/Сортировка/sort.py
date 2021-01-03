#! python
import os
import getpass
import platform
from pathlib import Path, PurePath

sort_dir = Path("D:\\test")  # Рабочая директория
cur_dir = Path.cwd()  # Текущая директория
file_list = []  # Список файлов
# Сопоставления файлов и директорий
un_sort = "__unsorted__"
folders = {
    "Видео": [".avi", ".flv", ".m4v", ".mkv"],
    "Музыка": [".mp3", ".flac"],
    "Изображения":
    [".raw", ".jpg", ".jpeg", ".tiff", ".psd", ".bmp", ".gif", ".png"],
    "Документы": [
        ".doc", ".docx", ".txt", ".rtf", ".pdf", ".fb2", ".djvu", ".xls",
        ".xlsx"
    ],
    "Архивы": [".rar", ".zip", ".7z"],
    un_sort: []
}

type_os = platform.system()  # Платформа
usernane = getpass.getuser()  # Имя пользователя


def create_dirs(sort_dir=sort_dir, folders=folders):
    ''' Создаем под директории '''
    for dirs in folders:
        new_dirs = Path(dirs)
        try:
            Path.mkdir(sort_dir / new_dirs)
        except FileExistsError as e:
            pass
        except PermissionError:
            print(f"Ошибка доступа: {new_dirs}")


def move_file(sort_dir=sort_dir, file_list=file_list, folders=folders):
    try:
        # Получаем список файлов
        for x in sort_dir.iterdir():
            if x.is_file():
                file_list.append(x)
            elif x.is_dir():
                pass
        if not file_list:
            print("Нет Файлов!")
            exit()
    except Exception as e:
        print("Нет Доступа!!! {}".format(e))
        exit()

    # Перемещаем файлы
    for fl in file_list:
        fl_name = PurePath(fl).name  # Имя файла
        ext = PurePath(fl).suffix  # Расширение

        for folder, ext_list in folders.items():
            target = sort_dir / folder / fl_name
            un_target = sort_dir / un_sort / fl_name  # для всего что не сортируется
            try:
                if ext in ext_list:
                    fl.rename(target)  # replace
                    print(f"{fl_name}")
                else:
                    pass
            except PermissionError:
                print(f"Ошибка доступа: {target}")
            except FileExistsError:
                print(f"Такой файл есть: {target}")


def main():
    create_dirs()
    move_file()


main()
