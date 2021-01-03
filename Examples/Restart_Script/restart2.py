import multiprocessing, time, sys

def main(event, args):
    """скрипт Python с аргументами на входе"""
    print(f'run {multiprocessing.current_process().name} {args}')
    time.sleep(2)
    event.set()  # При определённых условиях ему необходимо перезапустить самого себя

    time.sleep(2)
    print(f'normal stop {multiprocessing.current_process().name}')
    return

def main_restart(event, args, proc=None):
    """перезапуск скрипта"""
    # while True:
    for _ in range(10):
        event.wait()
        event.clear()
        if proc is not None:
            print(f'terminate {proc.name}')
            proc.terminate()

        proc = multiprocessing.Process(target=main, args=(event, args), daemon=True)
        proc.start()
    return

if __name__ == '__main__':
    Event = multiprocessing.Event()
    Event.set()
    main_restart(Event, sys.argv)