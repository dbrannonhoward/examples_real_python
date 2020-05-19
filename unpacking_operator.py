def generate_list_of_nums():
    list_of_nums = list()
    for i in range(7):
        list_of_nums.append(i)
    return list_of_nums


def print_starting_list(some_list):
    print('starting list is ' + str(some_list))


def unpack_a_list(*call_with_unpacker):
    print(str(call_with_unpacker) + ' is a tuple, immutable')


def unpack_trick_01(some_list):
    a, *b, c = some_list
    print('a is ' + str(a))
    print('b is ' + str(b))
    print('c is ' + str(c))


def sum_any_length_list(*integers):
    sum_total = 0
    for integer in integers:
        sum_total += integer
    return 'the sum is ' + str(sum_total)


def main():
    list_of_nums = generate_list_of_nums()
    print_starting_list(list_of_nums)
    unpack_trick_01(list_of_nums)
    unpack_a_list(*list_of_nums)
    print(sum_any_length_list(*list_of_nums))


if __name__ == '__main__':
    main()
