import twilio.rest
import dotenv

dotenv.load_dotenv()  # Load environment variables from .env file
my_account_sid = dotenv.get_key(".env", "MY_ACCOUNT_SID")
my_auth_token = dotenv.get_key(".env", "MY_AUTH_TOKEN")
my_whatsapp_number = dotenv.get_key(".env", "MY_WHATSAPP_NUMBER")

#1. Credentials
account_sid = my_account_sid
auth_token = my_auth_token

# 2. Initialize the client
client = twilio.rest.Client(account_sid, auth_token)

# 3. Send the message
message = client.messages.create(
    from_="whatsapp:+14155238886",  # Twilio Sandbox number
    to=f"whatsapp:{my_whatsapp_number}",  # Include your country code!
    body="Hello from my Python bot! 🚀",
)

# 4. Print confirmation
print(f"Message sent! ID: {message.sid}")
print(f"Message sent! ID: {message.sid}")
