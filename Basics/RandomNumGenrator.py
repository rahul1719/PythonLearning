from random import randint

for i in range(0, 1000000):
    print(randint(0, 1000000))
    list.__add__(randint(0, 1000000))
print(list)
