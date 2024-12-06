import yfinance as yf
import plyer as pl


# Função para buscar os dados do ativo
def historia(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

def pegaBTC():
    codigo = ["BTC-USD"]
    inicio = "2024-12-04"

    for btc in codigo:
        print(f"Analizando {btc}")
        data = historia(codigo, inicio)