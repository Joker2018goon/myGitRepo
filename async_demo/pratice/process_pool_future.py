from concurrent.futures import ProcessPoolExecutor
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
    # process_list = []
    logging.debug('multi process....')
    start = time.time()
    with ProcessPoolExecutor() as excutor:
        # r :area
        # zip: k->v
        for r, area in zip(r_list, excutor.map(circle_area, r_list)):
            print(f'{r}:{area}')

    print('multi processes time:', (time.time() - start) * 1000)


def get_area_one_processes():
    # process_list = []
    logging.debug('one process....')
    start = time.time()
    for r, area in zip(r_list, map(circle_area, r_list)):
        print(f'{r}:{area}')

    print('one processes time:', (time.time() - start) * 1000)


def main():
    # log_to_stderr()
    # get_logger()
    get_area_multi_processes()
    get_area_one_processes()


if __name__ == '__main__':
    main()