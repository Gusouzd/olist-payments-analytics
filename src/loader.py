from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig, WriteDisposition
import logging
import os

def carregar_tabelas(df, nome_tabela):

    client = bigquery.Client(project=os.environ["GCP_PROJECT_ID"])
    destino = f'{os.environ["GCP_PROJECT_ID"]}.raw_olist.{nome_tabela}'
    config = LoadJobConfig(
            write_disposition=WriteDisposition.WRITE_TRUNCATE
        )

    try:
        job = client.load_table_from_dataframe(df, destino, job_config=config)
        job.result()
        tabela = client.get_table(destino)
        logging.info(f"{nome_tabela} carregada — {tabela.num_rows} linhas")
    except Exception as e:
        logging.error(f"Erro ao carregar tabela {nome_tabela} no BigQuery: {e}")
        raise