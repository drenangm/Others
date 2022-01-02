import pandas as pd
import pytz
from datetime import datetime
from typing import List

#Substituiu a vírgula pelo ponto nos floats
def remove_incorret_chars(listas : List) -> List:
    filtered_list = []
    for n in listas:
        n = n.replace(',', '.')
        n = float(n)
        filtered_list.append(n)

    return filtered_list

#Filtra os valores de venda
def filter_vendas(df : pd.DataFrame) -> pd.DataFrame:
    lista = df['VENDAS'].tolist()
    lista = remove_incorret_chars(lista)
    df.drop('VENDAS', axis=1, inplace=True)
    df['VENDAS'] = lista

    return df

#Identifica a abreviação do mês e converte para número
def short_month_to_number(month : str) -> int:
    DICT_MONTH = {
        'JAN' : 1,
        'FEV' : 2,
        'MAR' : 3,
        'ABR' : 4,
        'MAI' : 5,
        'JUN' : 6,
        'JUL' : 7,
        'AGO' : 8,
        'SET' : 9,
        'OUT' : 10,
        'NOV' : 11,
        'DEZ' : 12,
    }

    month_number = 0

    for key, value in DICT_MONTH.items():
        if key == month:
            month_number = value
            return month_number

    return None


#Cria a coluna com o ano e mês
def create_yearmonth_col(df : pd.DataFrame) -> None:
    df_clean = df.copy()
    df_years = df_clean['ANO'].tolist()
    df_months = df_clean['MÊS'].tolist()
    date_list = []
    for index, years in enumerate(df_years):
        month = short_month_to_number(df_months[index])
        date_list.append(datetime(years,month, 1).strftime("%Y-%m"))

    df_clean['year_month'] = date_list
    df_clean['year_month'] = df_clean['year_month'].astype('M').dt.strftime('%Y-%m')
    df_clean.drop('ANO', axis=1, inplace=True)
    df_clean.drop('MÊS', axis=1, inplace=True)

    return df_clean
    

#Cria a coluna com todas as unidades
def create_unit_col(df : pd.DataFrame) -> None:
    df_clean = df.copy()
    unit_list = []
    for n in range(len(df.index)):
        unit_list.append('m3')

    df_clean['unit'] = unit_list

    return df_clean


#Cria coluna com a data de execução
def create_created_date_col(df : pd.DataFrame) -> None:
    df_clean = df.copy()
    created_date_list = []
    tz = pytz.timezone("Brazil/East")
    for n in range(len(df.index)):
        created_date_list.append(datetime.now(tz).strftime("%Y-%m-%d-%H:%M:%S"))

    df_clean['created_at'] = created_date_list

    return df_clean

#Renomeia as colunas
def rename_cols(df : pd.DataFrame) -> None:
    df_clean = df.copy()
    df_clean.drop('GRANDE REGIÃO', axis=1, inplace=True)
    df_clean = df_clean[['year_month', 'UNIDADE DA FEDERAÇÃO', 'PRODUTO', 'unit', 'VENDAS', 'created_at']]
    df_clean = df_clean.set_axis(['year_month', 'uf', 'product', 'unit', 'volume', 'created_at'], axis=1, inplace=False)

    return df_clean