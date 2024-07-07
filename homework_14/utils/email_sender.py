from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import jinja2
import smtplib
import config

def send(
  recipients: list[str],
  *,
  body: str,
  subject: str,
  attachments: list[str] = None
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
