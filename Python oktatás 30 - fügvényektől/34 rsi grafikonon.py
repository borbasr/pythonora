import requests
import pandas as pd
import matplotlib.pyplot as plt

# --- Binance API lekérés ---
url = "https://api.binance.com/api/v3/klines"
params = {"symbol": "BTCUSDT", "interval": "1m", "limit": 500}
data = requests.get(url, params=params).json()

# --- DataFrame létrehozása ---
df = pd.DataFrame(data, columns=[
    "open_time","open","high","low","close","volume",
    "close_time","qav","num_trades","taker_base_vol",
    "taker_quote_vol","ignore"
])

# --- adattípusok konverziója ---
df["close"] = df["close"].astype(float)

# --- időbélyeg átalakítása Budapesti időre ---
df["time"] = pd.to_datetime(df["open_time"], unit="ms", utc=True)
df["time"] = df["time"].dt.tz_convert("Europe/Budapest")

# --- RSI függvény ---
def rsi(close: pd.Series, length: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1/length, min_periods=length, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/length, min_periods=length, adjust=False).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

# --- RSI kiszámítása ---
df["RSI_14"] = rsi(df["close"], 14)

# --- Ábra létrehozása: 2 alpanel (ár + RSI) ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12,8), sharex=True,
                               gridspec_kw={'height_ratios':[3,1]})

# Árfolyam-grafikon
ax1.plot(df["time"], df["close"], label="BTC/USDT árfolyam", color="dodgerblue")
ax1.set_title("BTC/USDT árfolyam és RSI (Binance 1h gyertyák)")
ax1.set_ylabel("Ár (USD)")
ax1.legend(loc="upper left")
ax1.grid(True, alpha=0.3)

# RSI-grafikon
ax2.plot(df["time"], df["RSI_14"], label="RSI (14)", color="orange")
ax2.axhline(70, color="red", linestyle="--", alpha=0.6, label="Túlvett (70)")
ax2.axhline(30, color="green", linestyle="--", alpha=0.6, label="Túladott (30)")
ax2.set_ylabel("RSI érték")
ax2.set_xlabel("Idő (Budapest)")
ax2.set_ylim(0,100)
ax2.legend(loc="upper left")
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
