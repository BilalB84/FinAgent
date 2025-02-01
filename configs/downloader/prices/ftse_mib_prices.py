import os
import yfinance as yf
import pandas as pd

# Percorso del file contenente la lista dei titoli
ASSET_LIST_PATH = os.path.join(os.path.dirname(__file__), '../../_asset_list/ftse_mib.txt')

# Percorso della cartella dove salvare i dati
DATA_SAVE_PATH = os.path.join(os.path.dirname(__file__), '../../data/ftse_mib_prices.csv')

def load_tickers():
    """Carica la lista dei titoli FTSE-MIB da file."""
    with open(ASSET_LIST_PATH, 'r') as f:
        tickers = [line.strip() for line in f.readlines() if line.strip()]
    return tickers

def download_prices(tickers):
    """Scarica i prezzi di chiusura storici da Yahoo Finance."""
    data = yf.download(tickers, period='1y', interval='1d', group_by='ticker')
    return data

def save_prices(data):
    """Salva i dati in formato CSV."""
    data.to_csv(DATA_SAVE_PATH)
    print(f"Dati salvati in {DATA_SAVE_PATH}")

def main():
    tickers = load_tickers()
    print(f"Scaricando i dati per {len(tickers)} titoli del FTSE-MIB...")
    prices = download_prices(tickers)
    save_prices(prices)

if __name__ == "__main__":
    main()
