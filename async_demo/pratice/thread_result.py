from queue import Queue
from threading import Thread

q_result = Queue()
str_list=['222','444','333','666','888']

def str_to_int(arg, queue):
    result = int(arg)
    queue.put({arg: result})

def main():
    thread_list=[]
    for s in str_list:
        t=Thread(target=str_to_int,args=(s,q_result))
        t.start()
        thread_list.append(t)

    for i in thread_list:
        i.join()

    # print(q_result)

    print([q_result.get() for _ in range(len(str_list))])

if __name__ == '__main__':
    main()