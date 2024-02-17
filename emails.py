import yagmail
from settings import SETTINGS as S


def send_email(subject, message):
    """Sends email with specified subject/body/recipients"""
    sender = yagmail.SMTP(S["email_sender"], S["email_password"])

    for recipient in eval(S["recipients"]):
        sender.send(recipient, subject, message)
