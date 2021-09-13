import request
import json

class api_country:
    '''
    En esta clase se va a formar toda la URL para la búsqueda de la información

    La idea es tener un método para traer la información de cada uno de los
    países de manera individual y luego hacer la url de filtro completa. Así
    obtenemos la información que necesitamos específicamente y podemos evaluar
    paso a paso cada una de los requisitos.

    métodos de la clase:

    region_list -> devuelve la lista de regiones
    NOTA: En la V2 es en la que vamos a trabajar
    single_country -> Devuelve un país de una región
    '''
    # URL = 'https://restcountries.com/v2/'
    URL = 'https://restcountries.com/v2/all?fields=region,name,capital,languages'

    @classmethod
    def country_list():
        response = request.get(URL)
        if response.status_code == 200:
            countries = []
            data = json.loads(response.text)
            for element in data:
                country = Country(element)
                countries.append(country)
        return countries
