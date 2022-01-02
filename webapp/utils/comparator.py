from typing import Any, List
import pandas as pd
import pyexcel

#Converte todos os valores da lista para inteiros
def convert_list_int(lista : List) -> List[Any]:
    converted_list = []
    for i in lista:
        try:
            converted_list.append(int(i))
        except ValueError:
            continue

    return converted_list

#Arredonda os valores
def remove_incorret_chars(listas : List[List]) -> List[List]:
    for lista in listas:
        for index, n in enumerate(lista):
            try:
                n = round(n)
                lista.pop(index)
                lista.insert(index, n)
            except TypeError:
                continue

    return listas


#Coleta dados da planilha principal
def get_planilha_data() -> pd.DataFrame:
    sheet = pyexcel.get_sheet(file_name='./csv_files/vendas-combustiveis-m3.xls', name_columns_by_row=0)
    xlsarray = sheet.to_array()
    df_vendas_comb = pd.DataFrame(remove_incorret_chars(xlsarray[53:66]), columns=xlsarray[52])
    df_vendas_diesel = pd.DataFrame(remove_incorret_chars(xlsarray[133:146]), columns=xlsarray[132])
    
    return df_vendas_comb, df_vendas_diesel


#Compara os totais entre os dados extraídos e o total presente na planilha principal, essa função é executada em toda chamada da API
def compare_totals(df_total_comb : pd.DataFrame = None, df_total_diesel : pd.DataFrame = None):
    df_vendas_comb, df_vendas_diesel = get_planilha_data()
    total_erros_comb = 0
    total_erros_diesel = 0
    years_vendas_comb = convert_list_int(df_vendas_comb.columns.values)
    years_vendas_diesel = convert_list_int(df_vendas_diesel.columns.values)
    df_comb_totals = df_vendas_comb.iloc[[-1]].values.tolist()[0][2:]
    df_diesel_totals = df_vendas_diesel.iloc[[-1]].values.tolist()[0][2:]
    
    if df_total_comb is not None:
        for index, year in enumerate(years_vendas_comb):
            df = df_total_comb.query(f'ANO == {year}')
            total = round(df['VENDAS'].sum())
            if total != df_comb_totals[index]:
                total_erros_comb += 1
                print(f'Discrepância encontrada, ano: {year}')

    if df_total_diesel is not None:
        for index, year in enumerate(years_vendas_diesel):
            df = df_total_diesel.query(f'ANO == {year}')
            total = round(df['VENDAS'].sum())
            if total != df_diesel_totals[index]:
                total_erros_comb += 1
                print(f'Discrepância encontrada, ano: {year}')

    if total_erros_comb or total_erros_diesel > 0:
        return False
    return True