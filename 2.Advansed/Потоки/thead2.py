import threading


def worker(x, event_for_wait, event_for_set):
    for i in range(5):
        event_for_wait.wait()  # Ожидание события
        event_for_wait.clear()  # Устанавливает флаг False
        print(x)
        event_for_set.set()  # Устанавливает событие = true для второго потока


# Инициализация событий
e1 = threading.Event()
e2 = threading.Event()

# Инициализация потоков
t1 = threading.Thread(target=worker, args=(0, e1, e2))
t2 = threading.Thread(target=worker, args=(1, e2, e1))

# Запуск потока
t1.start()
t2.start()

# Подключаем потоки к основному
t1.join()
t2.join()

# События
# Event.is_set() - проверяет внутренний флаг
# Event.set() - устанавливает значение внутреннего флага в True
# Event.clear() - сбрасывает внутренний флаг в False,
# Event.wait() - ожидает пока внутренний флаг станет = True
# Event.wait(timeout=1.5) - если timeout не равный None то будет продолжен после таймаута.
