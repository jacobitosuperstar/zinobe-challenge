from collections.abc import Iterable
from tabulate import tabulate
import pandas as pd
from sqlalchemy import create_engine


def SaveToSQLite(df:Iterable)->None:
    '''
    Guardado del dataframe en la base de datos de SQLite.

    Si la base de datos se encuentra creada, no vuelve a crear la conexión

    argumentos:
    df -> dataframe
    '''
    try:
        engine = create_engine('sqlite:///zinobe_challenge.db', echo=False)
        sqlite_connection = engine.connect()
        sqlite_table = "test"
        df.to_sql(sqlite_table, sqlite_connection, if_exists='fail')
        sqlite_connection.close()
        return print('Guardado el DF en la base de datos')
    except ValueError:
        return print('Ya existe la tabla que intentas escribir')

def SaveToJson(df:Iterable)->None:
    '''
    Guardando el dataframe en un archivo JSON

    argumentos:
    df -> dataframe
    '''
    df.to_json(r'zinobe_challenge.json',orient='index')
    return print('Archivo Json creado exitosamente')


def DataFrame(countries_list:list)->Iterable:
    '''
    Generador del dataframe.

    El dataframe se crea aleatoreamente eligiendo un país de una de las
    regiones y agregándolo a una lista que se habría de convertir en el nuevo
    dataframe más adelante

    Adicionalmente, este dataframe se guarda en la base de datos de SQLite y
    en un archivo json.

    argumentos:
    country_list -> Lista de países
    '''
    data = countries_list
    df = pd.DataFrame(
        data,
        columns = [
            'region',
            'name',
            'capital',
            'hashed_language',
        ]
    )
    unique_regions = df.region.unique()
    table = []
    for region in unique_regions:
        df_subregion = df[df['region'] == region]
        df_subregion = df_subregion.sample()
        table.append(df_subregion.values.tolist())
    clean_table = []
    for item in table:
        for element in item:
            clean_table.append(element)
    df = pd.DataFrame(
        clean_table,
        columns = [
            'región',
            'país',
            'capital',
            'lenguaje codificado',
        ]
    )
    print(tabulate(df,headers='keys',tablefmt='psql'))
    SaveToSQLite(df)
    SaveToJson(df)
    return df
