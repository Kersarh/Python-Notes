"""
Создаем один нейрон и проверяем на что он способен
"""


class Neuron:
    weight = 0.5  # Вес полученых данных
    smoothing = 0.0001  # Корректировка
    lasterror = 0  # Последняя ошибка

    # Нейрон
    def neur(self, a):
        return a * self.weight

    # Обратная обработка.
    def reverse_neur(self, a):
        return a / self.weight

    def train(self, a, b):
        """Тренировка нейрона
        a - входящие данные
        b - правильное значения
        """
        # Текущий результат работы нейрона
        actual_result = self.neur(a)

        # Ошибка в расчете нейрона
        self.lasterror = b - actual_result

        # Корректировка - на какую величину менять веса
        correction = (self.lasterror / actual_result) * self.smoothing
        self.weight += correction  # меняем вес статов


# Данные для обучения
km = 100
mil = 62.1371
nr = Neuron()

# Обучение
while True:
    # Если ошибка НЕ в пределах корректировки
    if round(nr.lasterror, 4) != nr.smoothing:
        nr.train(km, mil)
        print("error", nr.lasterror)
    else:
        print("ОБУЧЕНИЕ ЗАВЕРШЕНО")
        break

print("10км = ", nr.neur(10))
print("50км = ", nr.neur(50))
print("100км = ", nr.neur(100))
print("10ml = ", nr.reverse_neur(10))
