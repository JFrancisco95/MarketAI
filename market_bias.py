import yfinance as yf
from ta.momentum import RSIIndicator
from ta.trend import MACD
from gpt_assistant import chat_with_gpt

def get_market_bias():
  df = yf.download('NQ=F', period='1mo', interval='1d')
  df['SMA_20'] = df['Close'].rolling(window=20).mean()
  df['SMA_50'] = df['Close'].rolling(window=50).mean()
  df['RSI'] = RSIIndicator(df['Close']).rsi()
  macd = MACD(df['Close'])
  df['MACD'] = macd.macd()
  df['MACD_Signal'] = macd.macd_signal()
  df['MACD_Diff'] = df['MACD'] - df['MACD_Signal']

  lastest = df.iloc[-1]

  raw_facts = f"""Market Summary:
  Close: {lastest['Close']:.2f}
  SMA_20: {lastest['SMA_20']:.2f}
  SMA_50: {lastest['SMA_50']:.2f}
  RSI: {lastest['RSI']:.2f}
  MACD: {lastest['MACD']:.2f}
  """
  prompt = f"""Based on the following market data, provide a summary of the market bias and any potential risks or opportunities for Nasdaq Futures:
  {raw_facts}
  """
  summary = chat_with_gpt(prompt)
  return summary