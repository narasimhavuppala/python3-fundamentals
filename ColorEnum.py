from enum import Enum, unique,auto


#@unique
class Color(Enum):
    #RED = 1
    RED=auto()
    BLUE = 2
    ORANGE = 3
    NAVYBLUE=3

print(list(Color))
print(Color.BLUE._value_)
print(repr(Color.BLUE))
print (type(Color.RED))
print (isinstance(Color.RED,Color))

for sc in Color:
    print(sc)

print(Color(1))
print(Color['RED'])