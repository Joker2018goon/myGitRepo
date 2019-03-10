import time
import threading
from threading import Thread


def countdown(n,num):
    while n > 0:
        t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        print(t,f'第{num}个线程，倒数开始',threading.current_thread().name, n)
        n -= 1
        time.sleep(1)
        
# threading.current_thread 获取线程名
def work():
    print(threading.current_thread().name,'开始')
    time.sleep(2)
    print(threading.current_thread().name,'结束')

def main():
    Thread(target=work,name='joker-thread').start()
    for i in range(3):
        Thread(target=countdown, args=(5, i + 1)).start()


if __name__ == '__main__':
    main()