from twilio.rest import Client

account_sid = 'ACdcc2236233d7893f3895195ef8748d58'
auth_token = '195540631b942531192db4e1e731dce1'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+16812485955',
    body="Hi, do you want to eat something?",
    to='+919267939323'
)

print(message.sid)
