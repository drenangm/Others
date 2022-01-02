from fastapi import FastAPI
from threading import Thread
from webapp.services.filter_by_uf import create_files_by_uf_diesel, create_files_by_uf_combs
from webapp.utils.download_file import download_files
from webapp.services.filter_by_year import create_files_by_year_combs, create_files_by_year_diesel
from webapp.services.filter_by_product import create_files_by_product_combs, create_files_by_product_diesel
from webapp.services.query_by_year import query_by_year_combs, query_by_year_diesel
from webapp.services.query_by_uf import query_by_uf_combs, query_by_uf_diesel
from webapp.services.query_by_product import query_by_product_combs, query_by_product_diesel
import uvicorn
import os

app = FastAPI()

@app.get("/")
async def root():    
    return {"Raízen": "0.0.1"}


@app.get("/diesel/uf")
async def extract_uf_diesel():
    if not os.path.isdir('./csv_files'):
        print('Iniciado o download da fonte dos dados')
        download_files()
    x = Thread(target=create_files_by_uf_diesel)
    x.start()

    return {'Message' : 'Thread iniciada: Extração dados das vendas de diesel por UF'}


@app.get("/derivados/uf")
async def extract_uf_derivados():
    if not os.path.isdir('./csv_files'):
        print('Iniciado o download da fonte dos dados')
        download_files()
    x = Thread(target=create_files_by_uf_combs)
    x.start()

    return {'Message' : 'Thread iniciada: Extração dados das vendas dos derivados por UF'}

@app.get("/derivados/products")
async def extract_products_derivados():
    if not os.path.isdir('./csv_files'):
        print('Iniciado o download da fonte dos dados')
        download_files()
    x = Thread(target=create_files_by_product_combs)
    x.start()

    return {'Message' : 'Thread iniciada: Extração dados das vendas dos derivados por produto'}


@app.get("/diesel/products")
async def extract_products_diesel():
    if not os.path.isdir('./csv_files'):
        print('Iniciado o download da fonte dos dados')
        download_files()
    x = Thread(target=create_files_by_product_diesel)
    x.start()

    return {'Message' : 'Thread iniciada: Extração dados das vendas de diesel por produto'}


@app.get("/derivados/year/all")
async def extract_year_derivados_all():
    if not os.path.isdir('./csv_files'):
        print('Iniciado o download da fonte dos dados')
        download_files()
    x = Thread(target=create_files_by_year_combs)
    x.start()

    return {'Message' : 'Thread iniciada: Extração dados das vendas dos derivados por ano'}


@app.get("/diesel/year/all")
async def extract_year_diesel_all():
    if not os.path.isdir('./csv_files'):
        print('Iniciado o download da fonte dos dados')
        download_files()
    x = Thread(target=create_files_by_year_diesel)
    x.start()

    return {'Message' : 'Thread iniciada: Extração dados das vendas de diesel por ano'}

#Query URL's
@app.get("/derivados/year/{year}")
async def query_by_year_derivados(year : int):
    if not os.path.isdir('./csv_files'):
        print('Iniciado o download da fonte dos dados')
        download_files()
    df = query_by_year_combs(year)

    return df


@app.get("/diesel/year/{year}")
async def query_by_year_diesel_func(year : int):
    if not os.path.isdir('./csv_files'):
        print('Iniciado o download da fonte dos dados')
        download_files()
    df = query_by_year_diesel(year)

    return df


@app.get("/derivados/uf/{uf}")
async def query_by_uf_derivados(uf : str):
    if not os.path.isdir('./csv_files'):
        print('Iniciado o download da fonte dos dados')
        download_files()
    df = query_by_uf_combs(uf)

    return df


@app.get("/diesel/uf/{uf}")
async def query_by_uf_diesel_func(uf : str):
    if not os.path.isdir('./csv_files'):
        print('Iniciado o download da fonte dos dados')
        download_files()
    df = query_by_uf_diesel(uf)

    return df


@app.get("/derivados/product/{product}")
async def query_by_products_derivados_func(product : str):
    if not os.path.isdir('./csv_files'):
        print('Iniciado o download da fonte dos dados')
        download_files()
    df = query_by_product_combs(product)

    return df


@app.get("/diesel/product/{product}")
async def query_by_products_derivados_func(product : str):
    if not os.path.isdir('./csv_files'):
        print('Iniciado o download da fonte dos dados')
        download_files()
    df = query_by_product_diesel(product)

    return df


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5020)