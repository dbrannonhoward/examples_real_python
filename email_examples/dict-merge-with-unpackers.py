x = {'a': 1, 'b': 2}
y = {'x': 3, 'y': 4}

z = {**x, **y}
print(z)
# note in python 2 it'd be z = dict(x, **y)
