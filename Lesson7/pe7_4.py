
def get_ticker_by_company_name(company_name: str) -> str:
    file = open('pe7_4.txt', 'r')

    for x in file.readlines():
        split_rule: list = x.split(':')
        if split_rule[0] == company_name:
            return split_rule[1]

    return "Could not find a ticker."


def get_company_name_by_ticker(ticker: str) -> str:
    file = open('pe7_4.txt', 'r')

    for x in file.readlines():
        split_rule: list = x.split(':')
        print(split_rule)
        if split_rule[1] == ticker:
            return split_rule[0]

    return "Could not find a company."

print(
    get_ticker_by_company_name(
        input('Enter a company name: ')
    )
)

print(
    get_company_name_by_ticker(
        input('Enter a ticker: ')
    )
)

