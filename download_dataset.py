"""
Script para baixar o dataset Telco Customer Churn.
Execute dentro da pasta raiz do projeto.
"""
import os
import urllib.request
import pandas as pd

# URL do dataset
URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"

# Pasta de destino
output_dir = os.path.join("data", "raw")
output_file = os.path.join(output_dir, "Telco-Customer-Churn.csv")

# Criar pasta se nao existe
os.makedirs(output_dir, exist_ok=True)

print("Baixando dataset...")
print(f"URL: {URL}")
print(f"Destino: {output_file}")
print()

try:
    urllib.request.urlretrieve(URL, output_file)
    print("[OK] Download concluido!")
    print()

    # Verificar
    df = pd.read_csv(output_file)
    print(f"Shape: {df.shape[0]} linhas x {df.shape[1]} colunas")
    print(f"Colunas: {list(df.columns)}")
    print()
    print("Primeiras 5 linhas:")
    print(df.head())
    print()
    print("=" * 50)
    print("Dataset pronto! Arquivo salvo em data/raw/")
    print("=" * 50)

except Exception as e:
    print(f"[ERRO] Falha no download: {e}")
    print()
    print("Alternativa: baixe manualmente de:")
    print("https://www.kaggle.com/datasets/blastchar/telco-customer-churn")
    print("E coloque o CSV em data/raw/Telco-Customer-Churn.csv")
