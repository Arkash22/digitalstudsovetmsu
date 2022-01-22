

import time
import threading


def f():

    threading.Timer(10.0, f).start()  # Перезапуск через 10 секунд)
    print('time')

f()


