import datetime

csv_list: list = []
csv_path = 'inloggers.csv'


def write_to_csv_file():
    csv_file = open(csv_path, 'a')
    for row in csv_list:
        csv_file.write(';'.join(row))
    csv_file.close()


while True:
    current_date = datetime.datetime.now()

    name = str(input("Wat is je achternaam? "))

    if name == 'einde':
        write_to_csv_file()
        break

    initials = str(input("Wat zijn je voorletters? "))
    birth_date = str(input("Wat is je geboortedatum? "))
    email = str(input("Wat is je e-mail? "))

    csv_list.append([current_date.strftime('%A %d %B at %H:%M'), name, initials, birth_date, email, '\n'])
    print("=================================")
