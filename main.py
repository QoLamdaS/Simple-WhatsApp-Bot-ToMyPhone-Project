import twilio.rest
import dotenv, os

dotenv.load_dotenv()  # Load environment variables from .env file
my_account_sid = os.getenv("MY_ACCOUNT_SID")
my_auth_token = os.getenv("MY_AUTH_TOKEN")
my_whatsapp_number = os.getenv("MY_WHATSAPP_NUMBER")

#1. Credentials
account_sid = my_account_sid
auth_token = my_auth_token

# 2. Initialize the client
client = twilio.rest.Client(account_sid, auth_token)

# 3. Send the message
message = client.messages.create(
    from_="whatsapp:+14155238886",  # Twilio Sandbox number
    to=f"whatsapp:+62{my_whatsapp_number}",  # Include your country code!
    body="Hello from my Python bot! 🚀",
)

# 4. Print confirmation
print(f"Message sent! ID: {message.sid}")
