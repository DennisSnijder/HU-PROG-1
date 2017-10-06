my_sum: list = []

while True:
    user_sum = int(input('Please enter a numer to add to the total sum.'))

    if user_sum is 0:
        print("There are " + str(len(my_sum)) + " numbers appended, the total of the sum is: " + str(sum(my_sum)))
        break

    my_sum.append(user_sum)