import itertools
import string

permute = string.printable
permute = 'wes'

all_combos = list()
for combo in itertools.permutations(permute):
    all_combos.append(combo)
    print(combo)
print(str(all_combos.__len__()) + ' total permutations')
