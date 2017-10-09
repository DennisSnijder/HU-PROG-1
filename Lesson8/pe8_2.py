import random

def monopoly_throw(throws_in_a_row = 0):
    first_throw = random.randint(0, 10)
    second_throw = random.randint(0, 10)

    print(str(first_throw) + ' + ' + str(second_throw) + ' = ' + str(first_throw + second_throw))

    if first_throw == second_throw:
        print("first and second throw are equal, lets do another throw!")
        monopoly_throw(throws_in_a_row + 1)

monopoly_throw()