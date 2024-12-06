import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função para buscar os dados do ativo
def get_stock_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

# Função para implementar a estratégia de médias móveis
def moving_average_strategy(data):
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['Signal'] = np.where(data['SMA_20'] > data['SMA_50'], 1, 0)
    data['Position'] = data['Signal'].diff()
    return data

# Função para plotar os sinais de compra e venda
def plot_signals(data, symbol):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Preço Fechamento', alpha=0.5)
    plt.plot(data['SMA_20'], label='SMA 20', alpha=0.75, color='orange')
    plt.plot(data['SMA_50'], label='SMA 50', alpha=0.75, color='purple')

    # Ajusta os sinais de compra e venda para coincidir com os índices
    buy_signals = data[data['Position'] == 1]  # Filtra os pontos de compra
    sell_signals = data[data['Position'] == -1]  # Filtra os pontos de venda

    # Plota os sinais no gráfico
    plt.scatter(buy_signals.index, buy_signals['Close'], label='Compra', marker='^', color='green', alpha=1)
    plt.scatter(sell_signals.index, sell_signals['Close'], label='Venda', marker='v', color='red', alpha=1)

    plt.title(f'Sinais de Compra/Venda para {symbol}')
    plt.xlabel('Data')
    plt.ylabel('Preço')
    plt.legend()
    plt.grid()
    plt.show()

# Função principal
def main():
    symbols = ["BTC-USD"]
    #symbols = ["IVVB11.SA"]
    #symbols = ["AAPL34.SA", "GOGL34.SA", "PETR4.SA", "NVDC34.SA"]
    start_date = "2024-01-01"
    end_date = "2024-12-04"

    for symbol in symbols:
        print(f"Analisando {symbol}...")
        data = get_stock_data(symbol, start_date, end_date)
        data = moving_average_strategy(data)
        plot_signals(data, symbol)
        print(data[['Close', 'SMA_20', 'SMA_50', 'Signal', 'Position']].tail())

if __name__ == "__main__":
    main()
