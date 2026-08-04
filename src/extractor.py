import pandas as pd
import logging
from pathlib import Path

def extrair_tabelas(caminho):
    
    dataframes = {}

    pasta = Path(caminho)
    for arquivo in pasta.iterdir():
        nome = arquivo.stem
        nome = nome.replace('olist_', '').replace('_dataset', '')
        dataframes[nome] = pd.read_csv(arquivo)

    for nome, df in dataframes.items():
        if df.empty:
            raise ValueError(f"Tabela {nome} chegou vazia")
        
        for coluna in df.columns:
            if ('date' in coluna) or ('timestamp' in coluna):
                df[coluna] = pd.to_datetime(df[coluna], errors='coerce')

    return dataframes