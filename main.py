from bs4 import BeautifulSoup
from operator import itemgetter

import requests

population_url = 'https://www.worldometers.info/world-population/population-by-country/'


def main():
    page = requests.get(population_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table_rows = soup.find('table').find_all('tr')
    countries = []

    for row in table_rows[1:]:
        row_data = row.contents
        country_name = row_data[3].text
        country_population = int(row_data[5].text.replace(',', ''))
        countries.append((country_name, country_population))

    countries.sort(key=itemgetter(1), reverse=True)
    for name, pop in countries:
        print(f'{name}={pop}')


if __name__ == '__main__':
    main()
