from flask import Flask, render_template
import yfinance as yf
from datetime import datetime
import time

app = Flask(__name__)


@app.after_request
def no_cache(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

ASSETS = {
    "equities": [
        {"ticker": "^GSPC", "name": "S&P 500", "sub": "Equity Index"},
        {"ticker": "^IXIC", "name": "Nasdaq", "sub": "Equity Index"},
        {"ticker": "^DJI", "name": "Dow Jones", "sub": "Equity Index"},
        {"ticker": "^BVSP", "name": "Ibovespa", "sub": "Equity Index (BR)"},
        {"ticker": "^STOXX50E", "name": "Euro Stoxx 50", "sub": "Equity Index"},
    ],
    "renda_fixa": [
        {"ticker": "^TNX", "name": "US Treasury 10Y", "sub": "Yield", "is_yield": True},
        {"ticker": "^TYX", "name": "US Treasury 30Y", "sub": "Yield", "is_yield": True},
        {"ticker": "TLT", "name": "iShares 20+ Yr Bond", "sub": "ETF"},
        {"ticker": "IEF", "name": "iShares 7-10 Yr Bond", "sub": "ETF"},
        {"ticker": "LQD", "name": "iShares IG Corporate", "sub": "ETF"},
        {"ticker": "HYG", "name": "iShares High Yield", "sub": "ETF"},
    ],
    "energia": [
        {"ticker": "CL=F", "name": "Petróleo WTI", "sub": "Futuro"},
        {"ticker": "BZ=F", "name": "Petróleo Brent", "sub": "Futuro"},
        {"ticker": "NG=F", "name": "Gás Natural", "sub": "Futuro"},
        {"ticker": "XLE", "name": "Energy Select SPDR", "sub": "ETF setorial"},
    ],
    "commodities": [
        {"ticker": "GC=F", "name": "Ouro", "sub": "Futuro"},
        {"ticker": "SI=F", "name": "Prata", "sub": "Futuro"},
        {"ticker": "HG=F", "name": "Cobre", "sub": "Futuro"},
        {"ticker": "ZC=F", "name": "Milho", "sub": "Futuro"},
        {"ticker": "ZS=F", "name": "Soja", "sub": "Futuro"},
    ],
    "etfs": [
        {"ticker": "SPY", "name": "SPDR S&P 500", "sub": "ETF"},
        {"ticker": "QQQ", "name": "Invesco Nasdaq 100", "sub": "ETF"},
        {"ticker": "IWM", "name": "iShares Russell 2000", "sub": "ETF"},
        {"ticker": "VEA", "name": "Vanguard Developed", "sub": "ETF"},
        {"ticker": "EEM", "name": "iShares MSCI EM", "sub": "ETF"},
    ],
    "fx": [
        {"ticker": "BRL=X", "name": "USD/BRL", "sub": "FX"},
        {"ticker": "EURUSD=X", "name": "EUR/USD", "sub": "FX"},
        {"ticker": "GBPUSD=X", "name": "GBP/USD", "sub": "FX"},
        {"ticker": "JPY=X", "name": "USD/JPY", "sub": "FX"},
        {"ticker": "DX-Y.NYB", "name": "Dollar Index (DXY)", "sub": "Index"},
    ],
    "crypto": [
        {"ticker": "BTC-USD", "name": "Bitcoin", "sub": "Crypto"},
        {"ticker": "ETH-USD", "name": "Ethereum", "sub": "Crypto"},
        {"ticker": "SOL-USD", "name": "Solana", "sub": "Crypto"},
    ],
}

CAT_LABELS = {
    "equities":    {"pt": "Ações",       "en": "Equities",     "es": "Acciones"},
    "renda_fixa":  {"pt": "Renda Fixa",  "en": "Fixed Income", "es": "Renta Fija"},
    "energia":     {"pt": "Energia",     "en": "Energy",       "es": "Energía"},
    "commodities": {"pt": "Commodities", "en": "Commodities",  "es": "Commodities"},
    "etfs":        {"pt": "ETFs",        "en": "ETFs",         "es": "ETFs"},
    "fx":          {"pt": "FX",          "en": "FX",           "es": "FX"},
    "crypto":      {"pt": "Crypto",      "en": "Crypto",       "es": "Cripto"},
}

_cache = {"data": None, "ts": 0}
CACHE_TTL = 60


def fmt_num(v, dec=2):
    if v is None:
        return "—"
    s = f"{v:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_vol(v):
    if not v:
        return "—"
    if v >= 1e9:
        return fmt_num(v / 1e9, 1) + "B"
    if v >= 1e6:
        return fmt_num(v / 1e6, 1) + "M"
    if v >= 1e3:
        return fmt_num(v / 1e3, 0) + "K"
    return str(int(v))


def fmt_pct(v, pp=False):
    if v is None:
        return "—"
    sign = "+" if v >= 0 else ""
    suffix = " pp" if pp else "%"
    return f"{sign}{v:.2f}".replace(".", ",") + suffix


def build_sparkline(closes, is_up):
    pts = closes.tolist()
    color = "#1a7a4c" if is_up else "#cc4444"
    fill = "rgba(26,122,76,0.12)" if is_up else "rgba(204,68,68,0.12)"
    if len(pts) < 2:
        return {"line": "", "area": "", "color": color, "fill": fill}
    lo, hi = min(pts), max(pts)
    rng = hi - lo if hi > lo else 1
    n = len(pts)
    xy = []
    for i, val in enumerate(pts):
        x = (i / (n - 1)) * 140
        y = 32 - ((val - lo) / rng) * 28
        xy.append(f"{x:.1f},{y:.1f}")
    line = " ".join(xy)
    area = f"{line} 140,36 0,36"
    return {"line": line, "area": area, "color": color, "fill": fill}


def get_dashboard_data():
    now = time.time()
    if _cache["data"] is not None and now - _cache["ts"] < CACHE_TTL:
        return _cache["data"]

    flat = []
    for cat, items in ASSETS.items():
        for a in items:
            flat.append({**a, "category": cat})

    tickers = [a["ticker"] for a in flat]

    data = yf.download(
        tickers,
        period="1y",
        interval="1d",
        group_by="ticker",
        progress=False,
        auto_adjust=True,
        threads=True,
    )

    result = {cat: [] for cat in ASSETS.keys()}

    for a in flat:
        try:
            hist = data[a["ticker"]] if len(tickers) > 1 else data
            closes = hist["Close"].dropna()
            if len(closes) < 2:
                continue

            curr = float(closes.iloc[-1])
            prev = float(closes.iloc[-2])
            is_yield = a.get("is_yield", False)

            daily = (curr - prev) if is_yield else (curr / prev - 1) * 100

            month_idx = max(0, len(closes) - 22)
            month_val = float(closes.iloc[month_idx])
            v1m = (curr - month_val) if is_yield else (curr / month_val - 1) * 100

            year_val = float(closes.iloc[0])
            v1y = (curr - year_val) if is_yield else (curr / year_val - 1) * 100

            low = float(closes.min())
            high = float(closes.max())

            vol = 0
            try:
                volumes = hist["Volume"].dropna()
                if len(volumes) > 0:
                    vol = float(volumes.iloc[-1])
            except Exception:
                pass

            is_up = daily >= 0
            spark = build_sparkline(closes.tail(30), is_up)

            if is_yield:
                price_str = f"{curr:.2f}%".replace(".", ",")
                low_str = f"{low:.2f}%".replace(".", ",")
                high_str = f"{high:.2f}%".replace(".", ",")
            else:
                price_str = fmt_num(curr)
                low_str = fmt_num(low)
                high_str = fmt_num(high)

            result[a["category"]].append({
                "name": a["name"],
                "ticker": a["ticker"],
                "sub": a["sub"],
                "category": a["category"],
                "price_str": price_str,
                "daily_str": fmt_pct(daily, pp=is_yield),
                "v1m_str": fmt_pct(v1m, pp=is_yield),
                "v1y_str": fmt_pct(v1y, pp=is_yield),
                "low_str": low_str,
                "high_str": high_str,
                "vol_str": fmt_vol(vol),
                "daily_up": daily >= 0,
                "v1m_up": v1m >= 0,
                "v1y_up": v1y >= 0,
                "spark": spark,
            })
        except Exception as e:
            print(f"[!] {a['ticker']}: {e}")
            continue

    _cache["data"] = result
    _cache["ts"] = now
    return result


@app.route("/")
def index():
    data = get_dashboard_data()
    tile_tickers = ["^GSPC", "^IXIC", "^BVSP", "CL=F", "GC=F"]
    flat = [item for items in data.values() for item in items]
    tiles = []
    for t in tile_tickers:
        for item in flat:
            if item["ticker"] == t:
                tiles.append(item)
                break

    return render_template(
        "index.html",
        data=data,
        tiles=tiles,
        cat_labels=CAT_LABELS,
        updated_at=datetime.now().strftime("%d/%m/%Y %H:%M"),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
