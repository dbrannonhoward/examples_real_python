def myfunc(x, y, z):
    return x, y, z


tuple_vec = (1, 0, 1)
dict_vec = {'x': 9, 'y': 0, 'z': 9}


print(myfunc(*tuple_vec))
print(myfunc(**dict_vec))
