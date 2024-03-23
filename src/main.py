import deltalake
import polars as pl
import duckdb

# Definição de caminhos dos arquivos
CSV_PATH = './data/csv/data.csv'
DELTA_PATH = './data/delta_table'

# leitura de dataframe csv com Polars
df = pl.read_csv(CSV_PATH)

# criação de tabela delta 
df.write_delta(DELTA_PATH, mode="overwrite")

#leitura de tabela delta
delta_df = pl.read_delta(DELTA_PATH)

# consulta de dataframe com duckdb
duckdb.sql("SELECT id, full_name FROM delta_df where id = '6edc0c8e-f979-40cc-ac39-a31c92596a73' ").show()
