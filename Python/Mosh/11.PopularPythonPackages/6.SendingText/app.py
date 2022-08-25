import config
from twilio.rest import Client


client = Client(
    config.account_sid, config.auth_token
)

sent = client.messages.create(
    to="+8801316981090",
    from_="+15592057619",
    body="This is message"
)

print(sent.date_sent)
