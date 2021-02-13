import json

data = {
    "User": {
        "name": "admin",
        "specialization": "Full"
    },
    "User2": {
        "name": "user",
        "specialization": "none"
    }
}

# Запись в файл
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

# Преобразование к строке
json_string = json.dumps(data, indent=4)
print(json_string)

# Чтение из файла
with open("data_file.json", "r") as read_file:
    data2 = json.load(read_file)
print(data2)
