from twilio.rest import Client

account_sid = 'account_sid'
auth_token = 'auth token'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='generated mobile number',
    body="Hi, do you want to eat something?",
    to='Mobile number to be sent to'
)

print(message.sid)
print("Message Sent")
print("Success")
