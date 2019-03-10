import time
from threading import Thread


def countdown(n):
    while n > 0:
        print('倒数开始', n)
        n -= 1
        time.sleep(1)


def main():
    # countdown()
    Thread(target=countdown, args=(5, )).start()


if __name__ == '__main__':
    main()