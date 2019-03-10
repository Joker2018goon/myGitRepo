def printer():
    counter=0
    while True:
        string=(yield)
        print('[{0}]{1}'.format(counter,string))
        counter+=1

def main():
    pass

if __name__ == '__main__':
    # main()
    p=printer()
    next(p)
    while True:
        msg=input(">>")
        if msg:
            p.send(msg)
        else:
            break