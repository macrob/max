from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import jinja2
import smtplib
import config
import os


def add_attachment(msg: MIMEMultipart, attach: str) -> None:
    is_file_exist = os.path.isfile(attach)

    if not is_file_exist:
        print(f'File {attach} does not exist')

    if is_file_exist:
        basename = os.path.basename(attach)
        size = os.path.getsize(attach)

        attachment = attach
        file = MIMEBase('application', f'octet-stream; name={basename}')
        file.set_payload(open(attach, 'rb').read())

        file.add_header('Content-Description', attachment)

        file.add_header(
            'Content-Description', f'attachment; filename={attachment}, size={size}'
        )

        encoders.encode_base64(file)
        msg.attach(file)

def send(
    recipients: list[str], *, body: str, subject: str, attachments: list[str] = None
):
    TOKEN = config.SMTP_TOKEN
    USER = config.SMTP_USER
    SERVER = config.SMTP_SERVER

    FROM_EMAIL = config.EMAIL_WELCOME_FROM
    FROM_NAME = config.EMAIL_WELCOME_FROM_NAME

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f'{FROM_NAME} <{FROM_EMAIL}>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = USER
    msg['Return-Path'] = USER
    msg['X-Mailer'] = 'Python'

    text_to_send = MIMEText(body, 'html')
    msg.attach(text_to_send)

    if attachments:
        for attach in attachments:
            add_attachment(msg, attach)

    mail = smtplib.SMTP_SSL(SERVER)
    mail.login(USER, TOKEN)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()


def create_welcome_email(params: dict) -> str:
    file = 'email-welcome.html'

    loader = jinja2.FileSystemLoader(searchpath=config.PTH_TEMPLATES)
    enviroment = jinja2.Environment(loader=loader)

    template = enviroment.get_template(file)
    output = template.render(params)
    return output
