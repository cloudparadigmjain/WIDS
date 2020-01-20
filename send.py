from twilio.rest import Client
from twilio.rest import Client
message='Deauth DDOS attack detected,average signal of attacker is - 69.0dbm'

account_sid = '{Insert}'
auth_token = '{Insert}'
client = Client(account_sid, auth_token)

numbers_to_message = ['{Insert}','{Insert}','{Insert}']
for number in numbers_to_message:
    client.messages.create(
    body = message,
    from_ = '{Provided by Twilio}',
    to = number
    )


