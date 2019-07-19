import codecs
import re


def main():
    # Словарь
    t = {
        "##NAME##": "user",
        "##mail##": "1@2.3"
    }
    # Читаем исходный файл
    infile = codecs.open("orig.txt", "r", 'cp1251').read()
    # Открываем файл на запись
    with codecs.open("out.txt", "w", 'cp1251') as outf:
        # Проход по оригинальному файлу для каждой строки словаря
        # с сохраняем в туже переменную
        for item in t:
            infile = re.sub(item, t[item], infile)
        # Записываем в файл что получилось
        outf.write(infile)


if __name__ == "__main__":
    main()
