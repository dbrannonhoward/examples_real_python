import itertools
import string
from time import sleep
from timeit import timeit


def generate_all_permutations_of_list(some_list_of_characters):
    """
    :param some_list_of_characters:
        the list to be operated on by the permutation function
    :param return_list:
        determines if the list of permutations is returned
    :param return_length:
        determines if the length of the list of permutations is returned
    :return:
        returnList, returnLength
        00 : return None
        01 : return permutation list info as a string
        10 : return permutation length info as a string
        11 : return both info, as a string
    """
    list_of_permutations = list()
    timeit_command = 'itertools.permutations(' + str(some_list_of_characters) + ')'
    time_to_generate_list = timeit(timeit_command, number=10000)  #TODO why do these times seem wrong?
    print(str(time_to_generate_list) + ' time to generate list')
    all_permutations_of_list = itertools.permutations(some_list_of_characters)
    for permutation in all_permutations_of_list:
        list_of_permutations.append(permutation)
    number_of_permutations = len(list_of_permutations)


def get_english_alphabet_upper_and_lower():
    return string.ascii_letters


def time_eval(command_to_eval):
    command_to_eval = str(command_to_eval)
    operation_time = timeit(command_to_eval, number=10000)
    return 'operation time : ' + str(operation_time) + \
           ' for operation : ' + str(command_to_eval)


def main():
    character_pool = string.ascii_letters
    growing_list = list()
    for i in range(len(character_pool)):
        growing_list.append(character_pool[i])
        print('beginning list permutation ' + str(growing_list))
        generate_all_permutations_of_list(growing_list)
        print('loop ' + str(i) + ' completed')
        sleep(1)


if __name__ == '__main__':
    main()
