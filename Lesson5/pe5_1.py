def convert(Celsius: float) -> float:
    return Celsius * 1.8 + 32


def table(celsius: list):
    for i in celsius:
        outcome = convert(i)
        print(outcome, i, sep='\t')


print(table([10, 20, 30]))
