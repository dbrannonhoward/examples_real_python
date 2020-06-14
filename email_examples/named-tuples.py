from collections import namedtuple

# immutable
Car = namedtuple('Car', 'color mileage')

my_car = Car('red', 3812.4)

print(my_car.color)
print(my_car.mileage)
print('repr(my_car) is ' + str(repr(my_car)))

