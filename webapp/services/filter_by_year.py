from datetime import date
import pandas as pd
from ..utils.comparator import compare_totals
from ..utils.dataframe_utils import create_unit_col, create_yearmonth_col, create_created_date_col, rename_cols, filter_vendas
import os


#Limpa dataframe
def clean_dataframe(df : pd.DataFrame) -> pd.DataFrame:
    df_clean = create_yearmonth_col(df)
    df_clean = create_unit_col(df_clean)
    df_clean = create_created_date_col(df_clean)
    df_clean = rename_cols(df_clean)

    return df_clean


#Cria os arquivos por ano (derivados)
def create_files_by_year_combs() -> None:
    df_combs = pd.read_csv('./csv_files/data_source1.csv', delimiter=';')
    df_combs = filter_vendas(df_combs)
    compare_totals(df_total_comb = df_combs)
    df_combs_clean = clean_dataframe(df_combs)
    print(df_combs_clean.dtypes)
    try:
        os.mkdir('./year_files_combs')
    except FileExistsError:
        pass
    year_range = [i for i in range(1990, date.today().year + 1)]
    for year in year_range:
        filename = f'derivados_{year}'
        df = df_combs_clean[df_combs_clean['year_month'].str.contains(f"{year}")]
        if not df.empty:
            with open(f'./year_files_combs/{filename}.json', 'w', encoding='utf-8') as file:
                df.to_json(file, orient='records', force_ascii=False)
    print('Criado arquivos por ano: derivados')

#Cria os arquivos por ano (diesel)
def create_files_by_year_diesel() -> None:
    df_diesel = pd.read_csv('./csv_files/data_source0.csv', delimiter=';')
    df_diesel = filter_vendas(df_diesel)
    compare_totals(df_total_diesel = df_diesel)
    df_diesel_clean = clean_dataframe(df_diesel)
    print(df_diesel_clean.dtypes)
    try:
        os.mkdir('./year_files_diesel')
    except FileExistsError:
        pass
    year_range = [i for i in range(2013, date.today().year + 1)]
    for year in year_range:
        filename = f'diesel_{year}'
        df = df_diesel_clean[df_diesel_clean['year_month'].str.contains(f"{year}")]
        if not df.empty:
            with open(f'./year_files_diesel/{filename}.json', 'w', encoding='utf-8') as file:
                df.to_json(file, orient='records',force_ascii=False)
    print('Criado arquivos por ano: diesel')

