#!/usr/bin/env python
import requests, json

region_list = ['africa','americas','asia','europe','oceania']

def main():
    response = requests.get(
        'https://restcountries.com/v2/all?fields=region,name,capital,languages'
    )
    countries = []
    data = json.loads(response.text)
    for element in data:
        languages = element.get('languages')
        languages_names = []
        for language in languages:
            name = language.get('name')
            languages_names.append(name)
        country_info = [
            element.get('region'),
            element.get('name'),
            element.get('capital'),
            languages_names,
        ]
        countries.append(country_info)
    return print(countries[0])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
