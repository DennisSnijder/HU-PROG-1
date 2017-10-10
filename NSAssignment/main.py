def get_starting_station_input(station_list: list) -> str:
    input_station = input("Wat is je beginstation? : ")

    if input_station not in station_list:
        print('Dit is geen valide station, probeer het opnieuw.')
        return get_starting_station_input(station_list)

    return input_station


def get_end_station_input(station_list: list, starting_station: str) -> str:
    input_station = input("Enter your end station: ")

    if station_list.index(input_station) < stations.index(starting_station):
        print("End station should be after the starting station.")
        return get_end_station_input(station_list, starting_station)

    if input_station not in station_list:
        print('Dit is geen valide station, probeer het opnieuw.')
        return get_end_station_input(station_list, starting_station)

    return input_station


def get_journey_summary(station_list: list, starting_station: str, end_station: str) -> str:
    friendly_starting_station_index = station_list.index(starting_station) + 1
    friendly_end_station_index = station_list.index(end_station) + 1

    distance = abs(friendly_end_station_index - friendly_starting_station_index)
    journey_price = distance * 5

    summary = ""

    summary += "Het beginstation " + starting_station + " is het " + str(
        friendly_starting_station_index) + "e station in het traject \n"

    summary += "Het eindstation " + end_station + " is het " + str(
        friendly_end_station_index) + "e station in het traject \n"

    summary += "De afstand bedraagt " + str(distance) + " station(s) \n"
    summary += "De prijs van het kaartje is " + str(journey_price) + " euro.\n"
    summary += "Jij stapt in de trein in: " + starting_station + "\n"

    for x in range(friendly_starting_station_index, friendly_end_station_index - 1):
        summary += "-  " + station_list[x] + "\n"

    summary += "\nJij stapt uit in " + end_station + "\n"

    return summary


stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert",
            "Roermond", "Sittard", "Maastricht"]

starting_station = get_starting_station_input(stations)
end_station = get_end_station_input(stations, starting_station)

print(
    get_journey_summary(stations, starting_station, end_station)
)
