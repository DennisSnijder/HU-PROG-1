def read_text_file(file_name: str) -> str:
    text_stream = open(file_name)
    text = text_stream.read()
    text_stream.close()

    return text

card_numbers: list = read_text_file('cardnumbers.txt').splitlines()

print('This file counts ' + str(len(card_numbers)) + ' lines')

highest_number: str = max(card_numbers)
split_number: str = highest_number.split(',')
index: int = card_numbers.index(max(card_numbers))

print('The highest number is: ' + str(split_number[0]) + ' And is located at line number:  ' + str(index + 1))
