# para hacer los request de la página
import requests
# codificador json
import json
# librería de hashes
import hashlib


class Countries:
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
    def CountryList(self:object)->object:
        '''
        Devuelve la lista de objetos de los países con las características del
        ejercicio

        argumentos:
        el objeto mismo

        retorna:
        la lista de países de la siguiente manera
        country.region
        country.name
        country.capital
        country.languages
        country.HashedLanguage() -> método del objeto
        '''
        response = requests.get(self.URL)
        if response.status_code == 200:
            data = json.loads(response.text)
            country_list = []
            for country_info in data:
                country = Country(country_info)
                country_list.append(country)
            return country_list
        else:
            return {'message':'error en el request'}

class Country:
    '''
    Devuelve cada uno de los países presentes en la data descargada en
    CountryList con la siguiente información:

    region -> str
    nombre del país -> str
    idiomas en hash -> str
    '''
    def HashedLanguage(self:object)->str:
        '''
        Entrega hasheada la lista de lenguajes o el lenguaje único del país en
        un sólo string

        argumentos:
        lista de lenguajes.

        retorna:
        string con el hash
        '''
        languages_list = []
        for language in self.languages:
            name = language.get('name')
            languages_list.append(name)
        empty_string = ''
        for language in languages_list:
            empty_string += language
        hash_object = hashlib.sha1(empty_string.encode())
        hashed_language = hash_object.hexdigest()
        return hashed_language

    def __init__(self:object, data:dict)->object:
        self.region: ClassVar[str] = data.get('region')
        self.name: ClassVar[str] = data.get('name')
        self.capital: ClassVar[str] = data.get('capital')
        self.languages: ClassVar[str] = data.get('languages')
