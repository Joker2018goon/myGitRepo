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
    # Thread(target=work,name='joker-thread').start()
    thread_list=[]
    for i in range(3):
        t=Thread(target=countdown, args=(3, i + 1))
        t.start()
        thread_list.append(t)
        # t.join() # 线程等待，全跑完，再执行下个线程

    for t in thread_list:
        t.join()

if __name__ == '__main__':
    main()