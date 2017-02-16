from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC5206a8f6aada0fc461bcf8334665817b" 
AUTH_TOKEN = "5be2d8f1ceab31287c274d040c1b3799" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
message = client.messages.create(
    to="+919550233669", 
    from_="+15017250604", 
    body="This is the ship that made the Kessel Run in fourteen parsecs?", 
    media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg", 
)

print(message.sid)
