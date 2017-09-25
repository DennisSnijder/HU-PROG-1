user_input: str = "5-9-7-1-7-8-3-2-4-8-7-9"

user_input_list: list = list(
    map(int, user_input.split('-'))
)
user_input_list.sort()

user_input_max_value: int = max(user_input_list)
user_input_min_value: int = min(user_input_list)

user_input_length: int = len(user_input)
user_input_sum: int = sum(user_input_list)

user_input_average: float = user_input_sum / user_input_length

print('Sorted list of ints, ' + str(user_input_list))
print('Highest number in list: ' + str(user_input_max_value))
print('Lowest number in list: ' + str(user_input_min_value))
print('Amount of numbers in list: ' + str(user_input_length))
print('Sum of numbers in list: ' + str(user_input_sum))
print('Average number in list: ' + str(user_input_average))
