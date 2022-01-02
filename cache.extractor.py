from openpyxl import load_workbook
import pandas as pd

planilha = load_workbook('vendas-combustiveis-m3.xlsx')
sheet = planilha['Plan1']

#Extrai dados do cache das tabelas dinâmicas e cria um dataframe
def create_df_cache(cache):
    total = []
    cols = {}
    for i in cache.cacheFields:
        cols[i.name] = i.name

    for linhas in cache.records.r:
        linha = []
        for cll in linhas._fields:
            try:
                linha.append(cll.v)
            except AttributeError:
                linha.append(None)
        total.append(linha)
    df = pd.DataFrame(columns=cols, data=total)
    return df


#Verificar index das tabelas (Apenas necessário uma vez)
'''
for table in sheet._pivots:
    print(table.name)
'''
cx_pivot_oil = sheet._pivots[3].cache
cx_pivot_diesel = sheet._pivots[1].cache
df_diesel = create_df_cache(cx_pivot_diesel)
df_oil = create_df_cache(cx_pivot_oil)
