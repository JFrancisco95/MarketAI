from twilio.rest import Client
import os

def send_sms(message):
  try:
      client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
      message = client.messages.create(
          body=message,
          from_=os.getenv('TWILIO_PHONE_NUMBER'),
          to=os.getenv('RECIPIENT_PHONE_NUMBER')
      )
      print(f"Message sent: {message.sid}")

  except Exception as e:
    print(f"Failed to send SMS: {e}")