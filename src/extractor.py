import pandas as pd
import logging
from pathlib import Path

def extrair_tabelas(caminho):
    
    dataframes = {}

    pasta = Path(caminho)
    for arquivo in pasta.iterdir():
        nome = arquivo.stem
        nome = nome.replace('olist_', '').replace('_dataset', '')
        logging.info(f"Lendo {nome}...")
        dataframes[nome] = pd.read_csv(arquivo)
    logging.info("Arquivos lidos com sucesso.")

    logging.info("Validando os dados lidos...")
    for nome, df in dataframes.items():
        logging.info(f"{nome} — {len(df)} linhas lidas")
        if df.empty:
            raise ValueError(f"Tabela {nome} chegou vazia")
    
        for coluna in df.columns:
            if ('date' in coluna) or ('timestamp' in coluna):
                df[coluna] = pd.to_datetime(df[coluna], errors='coerce')
    
    logging.info(f"{nome} — tipos convertidos")

    logging.info("Validação concluída com sucesso.")

    return dataframes