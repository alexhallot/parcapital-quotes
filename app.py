from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)

STOCKS = ["AAPL", "META", "PBR", "IBIT", "NVDA"]

@app.route("/")
def index():
    quotes = []
    for symbol in STOCKS:
        ticker = yf.Ticker(symbol)
        info = ticker.fast_info
        quotes.append({
            "symbol": symbol,
            "price": round(info.last_price, 2),
            "currency": info.currency,
        })
    return render_template("index.html", quotes=quotes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
