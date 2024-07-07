import os
from dotenv import load_dotenv

import utils.email_sender as email_sender

def main():
  # recipients = ['epishkin.serg@gmail.com']
  # send_email(
  #   recipients,
  #   body='Hello, world!',
  #   subject='Hello, world!'
  # )
  email_body = email_sender.create_welcome_email({
    'username': 'Sergey',
    'course': 'Python Developer'
  })
  
  recipients = ['epishkin.serg@gmail.com']

  email_sender.send(
    recipients,
    body=email_body,
    subject='Hello, world!'
  )

  print(email_body)

if __name__ == '__main__':
  main()