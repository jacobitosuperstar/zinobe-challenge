from tabulate import tabulate
import pandas as pd
from sqlalchemy import create_engine


def DataFrame(countries_list:list)->object:
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
            'region',
            'name',
            'capital',
            'hashed_language',
        ]
    )
    print(df)
    # print(tabulate(df,headers='keys',tablefmt='psql'))
    # print(unique_regions)
    return df
