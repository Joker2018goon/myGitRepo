def todo(a):
    result = yield a
    print(a + ' is doing...')
    return result + ' is done.'


def doing(x):
    result = yield todo(x)
    print(result)


def doing_from(x):
    result = yield from todo(x)
    print(result)


def main():
    try:
        # g = doing('python')
        g=doing_from('python')
        g.send(None)
        g.send('python')
    except StopIteration:
        pass


if __name__ == '__main__':
    main()