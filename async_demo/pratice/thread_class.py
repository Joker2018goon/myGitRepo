import time
import threading
import logging
from threading import Thread

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)-10s: %(message)s')


def countdown(n):
    while n > 0:
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # print(t, f'{threading.current_thread().name}-倒数开始', n)
        # logging.debug(f'{t} {threading.current_thread().name}倒数开始:{n}')
        logging.debug(f'{t} 倒数开始:{n}')
        n -= 1
        time.sleep(1)


# threading.current_thread 获取线程名
def work():
    print(threading.current_thread().name, '开始')
    time.sleep(2)
    print(threading.current_thread().name, '结束')


class MyThread(Thread):
    def __init__(self, name, count):
        '''初始化，继承Thread'''
        Thread.__init__(self)
        self.name = name
        self.count = count

    def run(self):
        '''启动线程'''
        countdown(self.count)


def main():
    # Thread(target=work,name='joker-thread').start()
    thread_list = []
    logging.debug('start......')
    for i in range(3):
        # t = Thread(target=countdown, args=(3, ))
        t = MyThread(f'thread-{i+1}', 3)
        t.start()
        thread_list.append(t)
        # t.join() # 线程等待，全跑完，再执行下个线程

    for t in thread_list:
        t.join()

    logging.debug('end!')


if __name__ == '__main__':
    main()