spring: tuple = (3, 4, 5)
summer: tuple = (6, 7, 8)
autumn: tuple = (9, 10, 11)
winter: tuple = (12, 1, 2)


def get_season_by_month_number(month: int) -> str:
    if month in spring:
        return "It's spring"
    elif month in summer:
        return "It's summer"
    elif month in autumn:
        return "It's autumn"
    elif month in winter:
        return "It's winter"
    else:
        return 'This is not a valid number, choose a number between 1 and 12'


season = int(input('Enter a month number: '))
print(get_season_by_month_number(season))
