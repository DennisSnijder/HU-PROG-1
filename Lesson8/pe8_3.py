
def get_utf8_encoded_string(input: str):
    encoded_string_list = list()
    encoded_string = ''

    for x in list(input):
        encoded_string_list.append(ord(x) + 3)

    for x in encoded_string_list:
        encoded_string += chr(x)

    return encoded_string

print(
    get_utf8_encoded_string(
        input("Enter a name to encode: ")
    )
)