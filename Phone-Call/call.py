import os
from twilio.rest import Client
from dotenv import load_dotenv
# from twilio.twiml.voice_response import VoiceResponse, Say

# Load environment variables from .env file
load_dotenv()


# Access environment variables
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

call = client.calls.create(
    from_='5075166737',
    to='2142502343',
    url='https://handler.twilio.com/twiml/EHe42de6d710787089fafa84a8b6d1c522'
)