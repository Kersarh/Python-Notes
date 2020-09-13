import os
import configparser


def createConfig(path):
    config = configparser.ConfigParser()
    # создаем Секцию
    config.add_section("Settings")
    config.add_section("Group")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Group", "user", "test_user")

    with open(path, "w+") as config_file:
        config.write(config_file)


def testConfig(path):

    # если файла нет то создаем с стандартными настройками
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    # Читаем некоторые значения из конфиг файла
    font = config.get("Settings", "font")
    font_size = config.get("Settings", "font_size")
    print("font = %s" % font)
    print("font_size = %s" % font_size)

    # Меняем значения из конфиг файла
    config.set("Settings", "font_size", "20")

    # Удаляем значение из конфиг файла
    config.remove_option("Settings", "font_style")

    # Вносим изменения в конфиг файл
    with open(path, "w") as config_file:
        config.write(config_file)


path = "conf.ini"
testConfig(path)

os.system("pause" if os.name == "nt" else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
