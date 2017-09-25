list_of_strings: list = eval(input("Give in a list seperated by comma's : "))

if len(list_of_strings) < 10:
    print('The list should be at least 10 words long.')
    exit(1)

newList: list = []

for i in list_of_strings:
    if len(i) == 4:
        newList.append(i)

print(newList)
