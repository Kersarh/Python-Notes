"""
pickle реализует алгоритм сериализации и десериализации объектов Python.
pickle позволяет преобразовывать объекты Python в поток байтов,
а также преобразовывать поток байтов обратно в Python-объект.
В последствии поток байтов можно легко записать в файл.
"""

import pickle

# Мои данные
data = {1: "Первый", 2: "Второй", "name": "user"}

# Сохраняем в файл
with open("data.backup", "wb") as f:
    pickle.dump(data, f)

# Загружаем из файла
with open("data.backup", "rb") as f:
    load_data = pickle.load(f)

print(load_data)
"""
pickle.dump(obj, file, protocol=None, *, fix_imports=True) -
записывает сериализованный объект в файл.
Аргумент - protocol указывает используемый протокол.
По умолчанию = 3 с Python 3.8.6 используется 4 версия.
Записывать и загружать надо с одним и тем же протоколом.

pickle.dumps(obj, protocol=None, *, fix_imports=True) -
возвращает сериализованный объект. Без записи в файл.

pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict") -
загружает объект из файла.

pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict") -
загружает объект из потока байт.

Модуль pickle также имеет несколько исключений:

pickle.PickleError
pickle.PicklingError
pickle.UnpicklingError
"""
