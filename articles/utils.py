# articles/utils.py
import yfinance as yf
from .models import Article, Ticker

def fetch_and_create_articles():
    tickers = Ticker.objects.all()
    for ticker in tickers:
        stock = yf.Ticker(ticker.symbol)
        hist = stock.history(period='1d')
        latest_data = hist.iloc[-1]
        article_title = f"{ticker.symbol} Stock Data"
        article_body = (
            f"Ask Price: {latest_data['Close']}\n"
            f"Daily High: {latest_data['High']}\n"
            f"Daily Low: {latest_data['Low']}"
        )
        Article.objects.create(title=article_title, body=article_body)