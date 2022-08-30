from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/CREATE_NEW_CONSOLE
# and set the enviroment variable. See http://twilio.io/secure
account_sid = 'AC418160c82677188c6f4631fc98ec89b5'
auth_token = 'ca25af5ae8e8b67333518eaa3a0d118a'
client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    client.messages.create(
        body = f'Hi! Your user and verification code is {user_code}',
        from_= '+19786431631',
        to = f'{phone_number}'
    )
