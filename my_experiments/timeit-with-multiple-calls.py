from timeit import Timer


def call_commands_ten_times():
    throwaway_list = list()
    command = '([x * x for x in range(1000) if not x % 2])'
    for i in range(100):
        throwaway_list = eval(command)
        throwaway_list = list()  # reset value


def time_and_report_incremental_timestamps_for(command):
    pass


def time_command_with_lambda(command):  # fyi lambda adds overhead
    my_timer = Timer(lambda: eval(command))
    my_timer_operation_time = my_timer.timeit(number=100)
    print('operation_time : ' + str(my_timer_operation_time))


def time_lambda_overhead():
    non_lambda_timer = Timer('5*5')
    non_lambda_timer_operation_time = non_lambda_timer.timeit(number=10000)
    lambda_timer = Timer(lambda: 5*5)
    lambda_timer_operation_time = lambda_timer.timeit(number=10000)
    print('non_lambda time : ' + str(non_lambda_timer_operation_time))
    print('lambda time : ' + str(lambda_timer_operation_time))
    how_many_times_faster = lambda_timer_operation_time / non_lambda_timer_operation_time
    print('non_lambda is ' + str(how_many_times_faster) + ' times faster')


def main():
    time_command_with_lambda('call_commands_ten_times()')
    # time_lambda_overhead()
    pass


if __name__ == '__main__':
    main()
