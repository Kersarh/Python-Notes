from threading import Thread
import time


def worker(work, time_to_work):
    print(f"Начало: {work}")
    time.sleep(time_to_work)
    print(work, " - Готово")


thread1 = Thread(target=worker, args=("Задача 1", 5))
thread2 = Thread(target=worker, args=("Задача 2", 3))
thread1.start()
thread2.start()
# thread1.join() # Подключение к потоку
# thread2.join()

print("Код после потоков")
