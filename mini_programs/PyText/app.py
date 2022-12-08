from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)
call = client.messages.create(
    to = "number",
    from_ = "number",
    body="This is our first message"
)

