import os
from dotenv import load_dotenv

load_dotenv()


SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_TOKEN = os.getenv('SMTP_TOKEN')
SMTP_USER = os.getenv('SMTP_USER')

# WELCOME EMAIL FROM INFO
EMAIL_WELCOME_FROM = SMTP_USER
EMAIL_WELCOME_FROM_NAME = 'Serg'


PTH_PROJECT = os.path.dirname(__file__)
PTH_TEMPLATES = os.path.join(PTH_PROJECT, 'templates')
