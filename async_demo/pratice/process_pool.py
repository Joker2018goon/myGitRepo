from multiprocessing import Process, Pool
import math

r_list = [1, 3, 4, 5, 2, 6, 12]


def circle_area(r):
    '''圆形面积'''
    # print(f'半径为{r}的圆形面积', math.pi * r * r)
    return math.pi * r * r


def main():
    process_list = []
    
    p = Pool(3)
    for r in r_list:
        result=p.apply_async(circle_area, args=(r, ))
        process_list.append(result)

    for p in process_list:
        print(p.get())


if __name__ == '__main__':
    main()