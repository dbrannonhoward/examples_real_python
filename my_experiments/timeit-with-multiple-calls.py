from timeit import Timer


def call_command_ten_times():
    throwaway_list = list()
    command = '([x * x for x in range(1000) if not x % 2])'
    for i in range(100):
        throwaway_list = eval(command)
        throwaway_list = list()  # reset value


def time_and_report_incremental_timestamps_for(command):
    pass


def time_command_with_lambda(command_string):  # fyi lambda adds overhead
    my_timer = Timer(lambda: eval(command_string))
    my_timer_operation_time = my_timer.timeit(number=250)
    print('operation_time w/ lambda : ' + str(my_timer_operation_time))


def time_command_without_lambda(command_string):
    my_timer = Timer(stmt=command_string, setup='from __main__ import call_command_ten_times')
    my_timer_operation_time = my_timer.timeit(number=250)
    print('operation_time w/o lambda : ' + str(my_timer_operation_time))


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
    time_command_with_lambda('call_command_ten_times()')
    time_command_without_lambda('call_command_ten_times()')
    # time_lambda_overhead()
    pass


if __name__ == '__main__':
    main()
