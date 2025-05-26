from os import close
import yfinance as yf
from ta.momentum import RSIIndicator
from ta.trend import MACD
from gpt_assistant import chat_with_gpt


def get_market_bias():
  df = yf.download('NQ=F', period='3mo', interval='1d')

  close_prices = df['Close'].squeeze()

  df['SMA_20'] = close_prices.rolling(window=20).mean()
  df['SMA_50'] = close_prices.rolling(window=50).mean()
  df['RSI'] = RSIIndicator(close=close_prices).rsi()

  macd = MACD(close=close_prices)
  df['MACD'] = macd.macd()
  df['MACD_Signal'] = macd.macd_signal()
  df['MACD_Diff'] = df['MACD'] - df['MACD_Signal']

  df = df.dropna()
  if df.empty:
    return "Not enough data to determine market bias."

  latest = df.dropna().iloc[-1]

  raw_facts = f"""Market Summary:
  Close: {float(latest['Close'].item()):.2f}
  SMA_20: {float(latest['SMA_20'].item()):.2f}
  SMA_50: {float(latest['SMA_50'].item()):.2f}
  RSI: {float(latest['RSI'].item()):.2f}
  MACD: {float(latest['MACD'].item()):.2f}
  """
  prompt = f"""Based on the following market data, provide a concise summary of the market bias and any potential risks or opportunities for Nasdaq Futures. Limit your response to 3 sentences and keep it under 500 characters:
  {raw_facts}
  """
  summary = chat_with_gpt(prompt)
  summary = truncate_text(summary,500)  # Truncate to 500 characters
  return summary

def truncate_text(text, max_chars=500):
  if len(text) <= max_chars:
    return text 
  truncated = text[:max_chars]
  last_period = truncated.rfind('.')
  if last_period != -1 and last_period > max_chars * 0.5:
    truncated = truncated[:last_period + 1]
  else:
    truncated = truncated.rstrip() + '...'
  return truncated
