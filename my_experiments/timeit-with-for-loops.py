import timeit


def build_growing_command(growth_factor):
    command = '([x * x for x in range(' + str(growth_factor) + ') if not x % 2])'
    return command


def print_operation_time_of(command):
    operation_time = timeit.timeit(command, number=10000)
    print('operation time : ' + str(operation_time) + ' of operation : ' + command)


def main():
    for i in range(0, 1000, 100):
        growing_command = build_growing_command(i)
        print_operation_time_of(growing_command)
        pass


if __name__ == '__main__':
    main()
