from extractor import extrair_tabelas
from loader import carregar_tabelas
from dotenv import load_dotenv
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pipeline.log'),
        logging.StreamHandler()
    ]
)

load_dotenv()

caminho = os.environ["DATA_PATH"]

dataframes = extrair_tabelas(caminho)


for nome, df in dataframes.items():
    carregar_tabelas(nome, df)