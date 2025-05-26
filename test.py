from market_bias import get_market_bias
from sms_sender import send_sms

def test_send():
  bias = get_market_bias()
  print("Sending SMS...")
  print(bias)
  send_sms(bias)

if __name__ == "__main__":
  test_send()  