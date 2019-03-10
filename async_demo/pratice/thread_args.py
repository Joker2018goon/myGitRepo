import time
from threading import Thread


def countdown(n,num):
    while n > 0:
        t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        print(t,f'第{num}个线程，倒数开始', n)
        n -= 1
        time.sleep(1)
        

def main():
    for i in range(3):
        Thread(target=countdown, args=(5, i + 1)).start()


if __name__ == '__main__':
    main()