from extractor import extrair_tabelas
from loader import carregar_tabelas
from dotenv import load_dotenv
import os

load_dotenv()

caminho = os.environ["DATA_PATH"]

dataframes = extrair_tabelas(caminho)

for nome, df in dataframes.items():
    carregar_tabelas(nome, df)