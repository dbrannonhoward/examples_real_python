# check for class inheritance relationships with issubclass() built-in


class BaseClass:
    pass


class SubClass(BaseClass):
    pass


print('issubclass(SubClass, BaseClass)? : ' + str(issubclass(SubClass, BaseClass)))
print('issubclass(SubClass, object)? : ' + str(issubclass(SubClass, object)))
print('issubclass(BaseClass, SubClass)? : ' + str(issubclass(BaseClass, SubClass)))

