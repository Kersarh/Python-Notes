import time


def benchmark(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        fn()
        end = time.time()
        print(f"[*] Время выполнения: {end - start} секунд.")
        return fn()

    return wrapper


@benchmark
def fun():
    time.sleep(0.5)


fun()
