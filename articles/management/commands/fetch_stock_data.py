# articles/management/commands/fetch_stock_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model  # Import get_user_model
from articles.models import Article, Ticker  
import yfinance as yf

class Command(BaseCommand):
    help = 'Fetch stock data and create articles'

    def handle(self, *args, **kwargs):
        # Fetch the default author
        CustomUser = get_user_model()
        default_author = CustomUser.objects.get(username='admin')

        tickers = Ticker.objects.all()  

        for ticker in tickers:
            stock = yf.Ticker(ticker.symbol)

            # Fetch the stock data
            hist = stock.history(period='1d')
            latest_data = hist.iloc[-1]

            article_title = f"{ticker.symbol} Stock Data"
            article_body = (
                f"Ask Price: {latest_data['Close']}\n"
                f"Daily High: {latest_data['High']}\n"
                f"Daily Low: {latest_data['Low']}"
            )

            # Create an Article with the default author
            Article.objects.create(title=article_title, body=article_body, author=default_author)

        self.stdout.write(self.style.SUCCESS('Successfully fetched stock data for all tickers'))