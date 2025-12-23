import requests
import pandas as pd

# --- Binance API lekérés ---
url = "https://api.binance.com/api/v3/klines"
params = {"symbol": "BTCUSDT", "interval": "1m", "limit": 100}
data = requests.get(url, params=params).json()

# --- DataFrame létrehozás ---
df = pd.DataFrame(data, columns=[
    "open_time","open","high","low","close","volume",
    "close_time","qav","num_trades","taker_base_vol",
    "taker_quote_vol","ignore"
])

# --- típuskonverzió ---
df["close"] = df["close"].astype(float)

# --- időbélyeg átalakítás (ms → datetime) ---
df["time"] = pd.to_datetime(df["open_time"], unit="ms")

# --- RSI kiszámítása (14 periódus, kézzel, külső csomag nélkül) ---
def rsi(close: pd.Series, length: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1/length, min_periods=length, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/length, min_periods=length, adjust=False).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

df["RSI_14"] = rsi(df["close"], 14)

# --- csak az idő, ár és RSI kiírása ---
print(df[["time", "close", "RSI_14"]].tail(10))
