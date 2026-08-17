import twilio.rest
import dotenv

dotenv.load_dotenv()  # Load environment variables from .env file
api_key = dotenv.get_key(".env", "API_KEY")

#1. Credentials
account_sid = "YOUR_ACCOUNT_SID_HERE"
auth_token = "YOUR_AUTH_TOKEN_HERE"

# 2. Initialize the client
client = twilio.rest.Client(account_sid, auth_token)

# 3. Send the message
message = client.messages.create(
    from_="whatsapp:+14155238886",  # Twilio Sandbox number
    to="whatsapp:+YOUR_PHONE_NUMBER",  # Include your country code!
    body="Hello from my Python bot! 🚀",
)

# 4. Print confirmation
print(f"Message sent! ID: {message.sid}")
