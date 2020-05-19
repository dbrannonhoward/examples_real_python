def generate_list_of_nums():
    list_of_nums = list()
    for i in range(7):
        list_of_nums.append(i)
    return list_of_nums


def merge_dicts():
    print("\nmerge dicts")
    dict_a = {"first": "a", "second": "b"}
    dict_b = {"third": "c", "fourth": "d"}
    dict_merge = {**dict_a, **dict_b}
    print(dict_merge)


def merge_lists():
    print("\nmerge_lists")
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    list_merge = [*list_a, *list_b]
    print(list_merge)


def print_starting_list(some_list):
    print("\nprint_starting_list")
    print('starting list is ' + str(some_list))


def string_to_list(any_string):
    print("\nstring to list")
    list_string = [*any_string]
    print(list_string)


def string_to_list_bad(any_string):
    print("\nstring to list bad")
    *a, = any_string
    print(a)


def unpack_a_list(*call_with_unpacker):
    print("\nunpack_a_list")
    print(str(call_with_unpacker) + ' is a tuple, immutable')


def unpack_trick_01(some_list):
    print("\nunpack_trick_01")
    a, *b, c = some_list
    print('a is ' + str(a))
    print('b is ' + str(b))
    print('c is ' + str(c))


def unpack_trick_02():
    print("\nunpack_trick_02")
    a_list = list()
    for i in range(5):
        a_list.append(i)
    print(a_list)
    print(*a_list)


def sum_any_length_list(*integers):
    print("\nsum_any_length_list")
    sum_total = 0
    for integer in integers:
        sum_total += integer
    return 'the sum is ' + str(sum_total)


def main():
    list_of_nums = generate_list_of_nums()
    print_starting_list(list_of_nums)
    unpack_trick_01(list_of_nums)
    unpack_trick_02()
    merge_lists()
    merge_dicts()
    the_string = 'an orange subway car'
    string_to_list(the_string)
    string_to_list_bad(the_string)
    unpack_a_list(*list_of_nums)
    print(sum_any_length_list(*list_of_nums))


if __name__ == '__main__':
    main()
