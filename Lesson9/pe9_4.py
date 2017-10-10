import csv


def load_initial_csv_data(file_path: str):
    csv_file = open(file_path, 'w')

    initial_products: list = [
        ['Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'],
        ['121', 'ABC123', 'Highlight pen', '231', '0.56'],
        ['123', 'PQR678', 'Nietmachine', '587', '9.99'],
        ['128', 'ZYX163', 'Bureaulamp', '34', '19.95'],
        ['137', 'MLK709', 'Monitorstandaard', '66', '32.50'],
        ['271', 'TRS665', 'Ipad hoes', '155', '19.01']
    ]

    for row in initial_products:
        csv_file.write(';'.join(row) + '\n')
    csv_file.close()


def read_csv_with_header(file_path: str) -> list:
    csv_file = open(file_path, 'r')
    products = csv.DictReader(csv_file, delimiter=";")
    product_list = []

    for product in products:
        # parse all the values back to their valid data types.
        product['Artikelnummer'] = int(product['Artikelnummer'])
        product['Voorraad'] = int(product['Voorraad'])
        product['Prijs'] = float(product['Prijs'])

        product_list.append(product)

    return product_list


def get_most_expensive_item(product_list: list) -> dict:
    price_list: list = [product['Prijs'] for product in product_list]
    most_expensive_price = max(price_list)
    most_expensive_index = price_list.index(most_expensive_price)

    return product_list[most_expensive_index]


def get_least_inventory_item(product_list: list) -> dict:
    inventory_list: list = [product['Voorraad'] for product in product_list]
    least_inventory_amount = min(inventory_list)
    least_inventory_index = inventory_list.index(least_inventory_amount)

    return product_list[least_inventory_index]


def get_total_items(product_list: list) -> int:
    inventory_list: list = [product['Voorraad'] for product in product_list]
    return sum(inventory_list)


csv_path = 'products.csv'
load_initial_csv_data(csv_path)

product_list = read_csv_with_header(csv_path)
most_expensive = get_most_expensive_item(product_list)
least_inventory = get_least_inventory_item(product_list)
total_items = get_total_items(product_list)

print("Het duurste artikel is de " + most_expensive['Naam'] + " en die kost " + str(most_expensive['Prijs']) + " Euro")
print("Er zijn slechts " + str(least_inventory['Voorraad']) + " exemplaren in voorraad van het product met nummer "
      + str(least_inventory['Artikelnummer']))
print("In totaal hebben wij " + str(total_items) + " producten in ons magazijn liggen")