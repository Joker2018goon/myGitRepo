import time
from functools import wraps


class DecoTime:
    def __init__(self):
        pass

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kw):
            str_log = '函数{}开始运行...'.format(func.__name__)
            print(str_log)
            t1 = time.time()
            func(*args, **kw)
            t = time.time() - t1
            print(f'运行{func.__name__}共用时{int(t)}秒')
        return wrapper