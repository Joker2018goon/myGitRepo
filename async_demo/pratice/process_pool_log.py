from multiprocessing import Process, Pool, get_logger, log_to_stderr
import math
import logging
import time



logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)-10s: %(message)s')

r_list = [1, 3, 4, 5, 2, 6, 12]

def circle_area(r):
    '''圆形面积'''
    # print(f'半径为{r}的圆形面积', math.pi * r * r)
    return math.pi * r * r

def get_area_multi_processes():
    process_list = []
    logging.debug('multi process....')
    p = Pool(3)
    start=time.time()
    for r in r_list:
        result = p.apply_async(circle_area, args=(r, ))
        process_list.append(result)

    for p in process_list:
        print(p.get())

    print('multi processes time:',(time.time()-start)*1000)

def get_area_one_processes():
    process_list = []
    logging.debug('one process....')
    start=time.time()
    for r in r_list:
        result = circle_area(r)
        process_list.append(result)

    for p in process_list:
        print(p)

    print('one processes time:',(time.time()-start)*1000)

def main():
    log_to_stderr()
    get_logger()
    get_area_multi_processes()
    get_area_one_processes()

if __name__ == '__main__':
    main()