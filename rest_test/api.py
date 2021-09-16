# para hacer los request de la página
import requests
# codificador json
import json
# librería de hashes
import hashlib
# types
from collections.abc import Iterable
# time
from time import time


class Countries:
    '''
    En esta clase se va a formar toda la URL para la búsqueda de la información

    La idea es tener un método para traer la información de cada uno de los
    países de manera individual y luego hacer la url de filtro completa. Así
    obtenemos la información que necesitamos específicamente y podemos evaluar
    paso a paso cada una de los requisitos.

    métodos de la clase:

    CountryList -> devuelve la lista de países

    NOTA: En la V2 es en la que vamos a trabajar
    '''
    # URL = 'https://restcountries.com/v2/'
    URL = 'https://restcountries.com/v2/all?fields=region,name,capital,languages'

    @classmethod
    def CountryList(self:object)->Iterable:
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
        country.time -> tiempo tardado para calcular el objeto
        '''
        response = requests.get(self.URL)
        if response.status_code == 200:
            data = json.loads(response.text)
            country_list = []
            for country_info in data:
                # se quiere dejar por fuera del método la función de cálculo de
                # tiempo, pero hay problemas al agregar la propiedad al objeto
                # en la función del decorador
                t_start = time()*1000
                country = Country(country_info)
                t_end = time()*1000
                country.time = t_end - t_start
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
        self.time: ClassVar[int] = 0
