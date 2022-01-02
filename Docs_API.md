Documentation for ANP fuel sales data extraction
=======================
With this API you can extract the most recent available data about diesel sales and oil made products. The api is also ready to deploy with docker.

## Endpoints
### Diesel Sales
#### Create files by UF
`http://0.0.0.0:5020/diesel/uf`
This endpoint will create a json file containing the data about diesel sales for each UF there exists in the .xls file, at the ufs_files_diesel directory.

#### Create files by product
`http://0.0.0.0:5020/diesel/products`
This endpoint will create a json file containing the data about diesel sales for each product there exists in the .xls file, at the products_files_diesel directory.

#### Create files by year
`http://0.0.0.0:5020/diesel/year/all`
This endpoint will create a json file containing the data about diesel sales for each year there exists in the .xls file, at the year_files_diesel directory.

#### Query data by year
`http://0.0.0.0:5020/diesel/year/{year}`
This endpoint will return a json that contains the data about diesel sales for the year typed as a parameter in the URL.
#### Query data by UF
`http://0.0.0.0:5020/diesel/uf/{uf}`
This endpoint will return a json that contains the data about diesel sales for the UF typed as a parameter in the URL.

#### Query data by product
`http://0.0.0.0:5020/diesel/product/{product}`
This endpoint will return a json that contains the data about diesel sales for the product typed as a parameter in the URL.

### Oil products Sales
#### Create files by UF
`http://0.0.0.0:5020/derivados/uf`
This endpoint will create a json file containing the data about oil products sales for each UF there exists in the .xls file, at the ufs_files_combs directory.

#### Create files by product
`http://0.0.0.0:5020/derivados/products`
This endpoint will create a json file containing the data about oil products sales for each product there exists in the .xls file, at the products_files_combs directory.

#### Create files by year
`http://0.0.0.0:5020/derivados/year/all`
This endpoint will create a json file containing the data about oil products sales for each year there exists in the .xls file, at the year_files_combs directory.

#### Query data by year
`http://0.0.0.0:5020/derivados/year/{year}`
This endpoint will return a json that contains the data about oil products sales for the year typed as a parameter in the URL.

#### Query data by UF
`http://0.0.0.0:5020/derivados/uf/{uf}`
This endpoint will return a json that contains the data about oil products sales for the UF typed as a parameter in the URL.

#### Query data by product
`http://0.0.0.0:5020/derivados/product/{product}`
This endpoint will return a json that contains the data about oil products sales for the product typed as a parameter in the URL.

