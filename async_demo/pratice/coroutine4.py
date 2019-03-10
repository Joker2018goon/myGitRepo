import time
import asyncio
import inspect


def todo(a):
    result = yield a
    print(a + ' is doing...')
    return result + ' is done.'


def doing(x):
    result = yield todo(x)
    print(result)

@asyncio.coroutine
def doing_from(x):
    result = yield from todo(x)
    print(result)


def main():
    print('doing_from:',inspect.iscoroutinefunction(doing_from))
    print('doing_from:',inspect.isgeneratorfunction(doing_from))
    try:
        # g = doing('python')
        g=doing_from('python')
        g.send(None)
        g.send('java')
    except StopIteration:
        pass


if __name__ == '__main__':
    main()