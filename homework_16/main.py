import config
import csv


def get_airports_by_country(filename: str, country: str) -> list[str]:
  DELIMITER = ';'

  with open(config.PTH_PROJECT + filename, mode='r', encoding='utf8') as file:
      reader = csv.DictReader(file, delimiter=DELIMITER)
      result = [airport['name'] for airport in reader if airport['iso_country'] == country]

  return result

def show_airports(airports: list[str], country: str) -> None:
    print(f'В списке {len(airports)} аэропортов из {country}')

    for airport in airports:
      print(airport)
def main():
    filename = 'airport-codes_csv.csv'
    airport_ua = get_airports_by_country('/' + filename, 'UA')
    show_airports(airport_ua, 'Украина')
    # pprint(airport_ua, indent=4);


if __name__ == '__main__':
    main()
