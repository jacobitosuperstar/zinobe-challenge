#!/usr/bin/env python
from rest_test.api import Countries
from pandas_test.table import DataFrame


def main()->None:
    countries = Countries().CountryList()
    countries_list = []
    for country in countries:
        countries_list.append(
            [
                country.region,
                country.name,
                country.capital,
                country.HashedLanguage(),
            ]
        )

    DataFrame(countries_list)
    return None

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
