import dis


def greet(name):
    return 'hello, ' + str(name)


def _print(_func):
    print(_func)


def main():
    _func = greet('dan')
    _print(_func)
    _print(dis.dis(_func))


if __name__ == '__main__':
    main()
