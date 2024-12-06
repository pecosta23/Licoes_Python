import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função para buscar os dados do ativo
def get_stock_data(symbol, start_date, end_date):
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        if data.empty:
            print(f"Não foi possível obter dados para {symbol}. Verifique se o ticker está correto.")
            return None
        return data
    except Exception as e:
        print(f"Erro ao baixar dados de {symbol}: {e}")
        return None

# Função para calcular indicadores
def calculate_indicators(data):
    # Médias móveis
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    
    # Índice de Força Relativa (RSI)
    delta = data['Close'].diff().squeeze()  # Garantir que seja unidimensional
    gain = delta.clip(lower=0)  # Apenas os valores positivos
    loss = -delta.clip(upper=0)  # Apenas os valores negativos, convertidos para positivos
    
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # MACD (Linha de Sinal e Linha MACD)
    ema_12 = data['Close'].ewm(span=12, adjust=False).mean()
    ema_26 = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = ema_12 - ema_26
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    
    # Volume (indicador de tendência no volume)
    data['Volume_Signal'] = data['Volume'].rolling(window=20).mean()
    
    return data

def evaluate_signals(data):
    # Verifica as colunas presentes no DataFrame
    print("Colunas atuais no DataFrame:", data.columns)

    # Lista das colunas necessárias
    required_columns = ['Close', 'SMA_20', 'SMA_50', 'RSI', 'MACD', 'Signal_Line']

    # Verifica se todas as colunas necessárias estão presentes
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        print(f"Colunas ausentes: {missing_columns}")
        return data  # Retorna o data sem continuar se faltarem colunas

    # Se todas as colunas necessárias estiverem presentes, aplica dropna
    data = data.dropna(subset=required_columns)

    # Verifica novamente se o dropna foi bem-sucedido
    print("Após dropna, colunas restantes:", data.columns)
    
    # Calcula o indicador de Potencial de Crescimento
    data['Growth_Potential'] = (
        (data['Close'] > data['SMA_50']) &  # Preço acima da média móvel de 50 períodos
        (data['SMA_20'] > data['SMA_50']) &  # SMA de 20 períodos acima da de 50 períodos
        (data['RSI'] > 50) &  # RSI indicando força compradora
        (data['MACD'] > data['Signal_Line'])  # MACD acima da linha de sinal
    )
    
    return data

# Função para plotar os indicadores e sinais
def plot_signals(data, symbol):
    plt.figure(figsize=(14, 7))

    # Preço e médias móveis
    plt.plot(data['Close'], label='Preço Fechamento', alpha=0.5)
    plt.plot(data['SMA_20'], label='SMA 20', alpha=0.75, color='orange')
    plt.plot(data['SMA_50'], label='SMA 50', alpha=0.75, color='purple')

    # Sinais de compra e venda
    plt.scatter(data.index[data['Buy_Signal']], data['Close'][data['Buy_Signal']], 
                label='Compra', marker='^', color='green', alpha=1)
    plt.scatter(data.index[data['Sell_Signal']], data['Close'][data['Sell_Signal']], 
                label='Venda', marker='v', color='red', alpha=1)

    plt.title(f'Sinais de Compra/Venda para {symbol}')
    plt.xlabel('Data')
    plt.ylabel('Preço')
    plt.legend()
    plt.grid()
    plt.show()

    # Plot RSI
    plt.figure(figsize=(14, 5))
    plt.plot(data['RSI'], label='RSI', color='blue', alpha=0.7)
    plt.axhline(30, linestyle='--', color='green', alpha=0.5)
    plt.axhline(70, linestyle='--', color='red', alpha=0.5)
    plt.title(f'Índice de Força Relativa (RSI) para {symbol}')
    plt.xlabel('Data')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid()
    plt.show()

# Função principal
def main():
    symbols = ["PETR4.SA", "IVVB11.SA"]
    start_date = "2023-01-01"
    end_date = "2024-12-01"

    for symbol in symbols:
        print(f"Analisando {symbol}...")
        data = get_stock_data(symbol, start_date, end_date)
        if data is None:
            continue

        data = calculate_indicators(data)
        data = evaluate_signals(data)
        plot_signals(data, symbol)

        # Exibindo os últimos sinais
        print(data[['Close', 'SMA_20', 'SMA_50', 'RSI', 'MACD', 'Signal_Line', 'Buy_Signal', 'Sell_Signal']].tail())

if __name__ == "__main__":
    main()