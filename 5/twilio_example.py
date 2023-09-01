import os
from pathlib import Path

from dotenv import load_dotenv
from twilio.rest import Client


def main():
    user_phone = str.strip(input("Receiver's phone number: "))
    user_message = str.strip(input("Enter your message: "))
    send_message(user_phone, user_message)


def send_message(phone, message):
    account_sid, auth_token, sender_phone = get_env_vars()
    client = Client(account_sid, auth_token)
    sent_message = client.messages.create(body=message, to=phone, from_=sender_phone)
    print(sent_message.sid)


def get_env_vars():
    # get the path of env file
    env_path = Path(__file__).parent.joinpath(".env")

    # load env file
    load_dotenv(env_path)

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    sender_phone = os.getenv("TWILIO_PHONE_NO")
    return account_sid, auth_token, sender_phone


if __name__ == "__main__":
    main()
