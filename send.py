from twilio.rest import Client
from twilio.rest import Client
message='Deauth DDOS attack detected,average signal of attacker is - 69.0dbm'

account_sid = 'ACd6ba5ebf3f1e2b055379782e1a5bd812'
auth_token = '67da0928759cc5cae83016f63d35a7bb'
client = Client(account_sid, auth_token)

numbers_to_message = ['+919826159719','+918989438840','+919901914554']
for number in numbers_to_message:
    client.messages.create(
    body = message,
    from_ = '+19515434319',
    to = number
    )


