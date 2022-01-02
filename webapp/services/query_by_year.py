from datetime import date
from typing import List
import pandas as pd
from ..utils.comparator import compare_totals
from ..utils.dataframe_utils import create_unit_col, create_yearmonth_col, create_created_date_col, rename_cols, filter_vendas


#Limpa o dataframe
def clean_dataframe(df : pd.DataFrame) -> pd.DataFrame:
    df_clean = create_yearmonth_col(df)
    df_clean = create_unit_col(df_clean)
    df_clean = create_created_date_col(df_clean)
    df_clean = rename_cols(df_clean)

    return df_clean


#Filtra o dataframe por ano (derivados) e retorna o mesmo
def query_by_year_combs(year : int) -> List[dict]:
    df_combs = pd.read_csv('./csv_files/data_source1.csv', delimiter=';')
    df_combs = filter_vendas(df_combs)
    compare_totals(df_total_comb = df_combs)
    df_combs_clean = clean_dataframe(df_combs)
    print(df_combs_clean.dtypes)
    df = df_combs_clean[df_combs_clean['year_month'].str.contains(f"{year}")]
    if df.empty:
        return {'Message' : 'Nenhum item encontrado com o ano enviado'}
    return df.to_dict(orient='records')


#Filtra o dataframe por ano (diesel) e retorna o mesmo
def query_by_year_diesel(year : int) -> List[dict]:
    df_diesel = pd.read_csv('./csv_files/data_source0.csv', delimiter=';')
    df_diesel = filter_vendas(df_diesel)
    compare_totals(df_total_diesel = df_diesel)
    df_diesel_clean = clean_dataframe(df_diesel)
    print(df_diesel_clean.dtypes)
    df = df_diesel_clean[df_diesel_clean['year_month'].str.contains(f"{year}")]
    if df.empty:
        return {'Message' : 'Nenhum item encontrado com o ano enviado'}
    return df.to_dict(orient='records')