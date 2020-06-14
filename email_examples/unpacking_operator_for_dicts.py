from random import choice
from string import printable


def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result


def generate_some_dict():
    some_dict = dict()
    keywords = [str(i) for i in range(99) if i % 3 == 0]
    for word in keywords:
        some_dict[word] = choice(printable)
    return some_dict


def print_all_dict_keys(dict_in):
    keys = ''
    for key in dict_in:
        keys += str(key)
    print(keys)


def print_all_dict_values(dict_in):
    values = ''
    for value in dict_in:
        values += str(dict_in[value])
    print(values)


def main():
    some_dict = generate_some_dict()
    print_all_dict_keys(some_dict)
    print_all_dict_values(some_dict)
    print(concatenate(**some_dict))


if __name__ == '__main__':
    main()