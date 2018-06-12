# -*- encoding=UTF-8 -*-


def log(level, *args, **kvargs):
    def inner(func):
        def wrapper(*args, **kvargs):
            print level,'before calling:', func.__name__
            print 'args', args, 'kvargs', kvargs
            func(*args, **kvargs)
            print 'after calling:', func.__name__

        return wrapper
    return inner


@log(level='INFO')
def hello(name, age):
    print 'hello', name, age


if __name__ == '__main__':
    hello('ben', age=2)
