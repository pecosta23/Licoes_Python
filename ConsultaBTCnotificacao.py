import yfinance as yf
from plyer import notification  # Import correto para notificações
import time 

def pegaBTC():
    #ticker do BTC
    btc_ticker = yf.Ticker("BTC-USD")
    #últimos fechamentos
    data = btc_ticker.history(period="1d")
    #preço de fechamento mais recente
    ultimo_preco = data['Close'].iloc[-1]
    return ultimo_preco

def envia_notificacao(preco):
    notification.notify(
        title="Preço Atual do BTC-USD",
        message=f"O BTC-USD está em ${preco:.2f}",
        app_name="Monitor BTC",
        timeout=10 #20 segundos
    )

while True:
    preco_atual = pegaBTC()
    envia_notificacao(preco_atual)
    time.sleep(100)#5min
