import pandas as pd
from ..utils.comparator import compare_totals
from ..utils.dataframe_utils import create_unit_col, create_yearmonth_col, create_created_date_col, rename_cols, filter_vendas
import os
import unidecode


#Limpa o dataframe
def clean_dataframe(df : pd.DataFrame) -> pd.DataFrame:
    df_clean = create_yearmonth_col(df)
    df_clean = create_unit_col(df_clean)
    df_clean = create_created_date_col(df_clean)
    df_clean = rename_cols(df_clean)

    return df_clean

#Cria os arquivos por produto (derivados)
def create_files_by_product_combs() -> None:
    df_combs = pd.read_csv('./csv_files/data_source1.csv', delimiter=';')
    df_combs = filter_vendas(df_combs)
    compare_totals(df_total_comb = df_combs)
    df_combs_clean = clean_dataframe(df_combs)
    product_list_combs = df_combs_clean['product'].unique()
    print(df_combs_clean.dtypes)
    try:
        os.mkdir('./products_files_combs')
    except FileExistsError:
        pass

    for product in product_list_combs:
        filename = unidecode.unidecode(product.lower().replace(' ', '_'))
        df = df_combs_clean.query(f'product == "{product}"')
        with open(f'./products_files_combs/{filename}.json', 'w', encoding='utf-8') as file:
            df.to_json(file, orient='records', force_ascii=False)


#Cria os arquivos por produto (diesel)
def create_files_by_product_diesel() -> None:
    df_diesel = pd.read_csv('./csv_files/data_source0.csv', delimiter=';')
    df_diesel = filter_vendas(df_diesel)
    compare_totals(df_total_diesel = df_diesel)
    df_diesel_clean = clean_dataframe(df_diesel)
    product_list_diesel = df_diesel_clean['product'].unique()
    print(df_diesel_clean.dtypes)
    try:
        os.mkdir('./products_files_diesel')
    except FileExistsError:
        pass

    for product in product_list_diesel:
        filename = unidecode.unidecode(product.lower().replace(' ', '_'))
        df = df_diesel_clean.query(f'product == "{product}"')
        df.to_json(f'./products_files_diesel/{filename}.json', orient='records')

