from bs4 import BeautifulSoup
from dataclasses import dataclass

import requests

population_url = 'https://www.worldometers.info/world-population/population-by-country/'
gdp_url = 'https://www.worldometers.info/gdp/gdp-by-country/'


@dataclass
class Country:
    ranking_position: int
    name: str
    gdp: int
    gdp_readable: str
    gdp_growth: float
    population: int
    gdp_per_capita: int
    share_of_global_gdp: float


def main():
    page = requests.get(gdp_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table_rows = soup.find('table').find_all('tr')
    countries = []

    for row in table_rows[1:]:
        row_data = [d.text for d in row.find_all('td')]

        country = Country(
            ranking_position=int(row_data[0]),
            name=row_data[1],
            gdp=int(row_data[2].replace('$', '').replace(',', '')),
            gdp_readable=row_data[3],
            gdp_growth=float(row_data[4].replace('%', '')),
            population=int(row_data[5].replace(',', '')),
            gdp_per_capita=int(row_data[6].replace('$', '').replace(',', '')),
            share_of_global_gdp=float(row_data[7].replace('%', '')),
        )
        countries.append(country)

    for country in countries:
        print(country)


if __name__ == '__main__':
    main()
