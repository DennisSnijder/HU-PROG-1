names: dict = {}

while True:
    name = input("Enter a name: ")

    if name == '':
        for name in names:
            print("There are " + str(names[name]) + " students with the name " + str(name))
        break
    elif name in names:
        names[name] += 1
    else:
        names[name] = 1
