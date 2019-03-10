from multiprocessing import Process
import math


r_list= [1,3,4,5,2,6,12]

def circle_area(r):
    '''圆形面积'''
    print(f'半径为{r}的圆形面积', math.pi * r * r)
    return math.pi * r * r


def main():
    process_list=[]
    for r in r_list:
        p = Process(target=circle_area, args=(r, ))
        p.start()
        process_list.append(p)
        

    for p in process_list:
        p.join()


if __name__ == '__main__':
    main()