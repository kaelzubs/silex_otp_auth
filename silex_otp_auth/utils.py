from twilio.rest import Client
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# Your Account Sid and Auth Token from twilio.com/CREATE_NEW_CONSOLE
# and set the enviroment variable. See http://twilio.io/secure
account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']

client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    client.messages.create(
        body = f'Hi! Your user and verification code is {user_code}',
        from_= '+19786431631',
        to = f'{phone_number}'
    )
