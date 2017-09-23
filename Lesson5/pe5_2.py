
def read_text_file(file_name: str) -> str:
    text_stream = open(file_name)
    text = text_stream.read()
    text_stream.close()

    return text

card_numbers = read_text_file('cardnumbers.txt').splitlines()

for x in card_numbers:
    name = x.split(',')
    print(name[1] + ' has card number ' + name[0])