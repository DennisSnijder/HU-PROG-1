amount = 4356.00

try:
    people = int(input('Met hoeveel mensen ben je: '))
    if people < 0:
        raise RuntimeError()
    print(amount / people)
except ZeroDivisionError:
    print('Delen door nul kan niet!')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except RuntimeError:
    print('Negatieve getallen zijn niet toegestaan!')
except:
    print('Onjuiste invoer!')