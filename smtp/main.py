import smtplib
from email.mime.text import MIMEText

smtp_server = "email-smtp.eu-north-1.amazonaws.com"
port = 587
username = "AKIAW7BGMTRC7XGULDNE"
password = "BP5DzUcS7NxGb4Vg0FrvNfzZGnhIDi0Atp8dYnlbPMdo"

# Создание текстового сообщения
msg = MIMEText("This is a test email.")
msg["Subject"] = "Test SMTP"
msg["From"] = 'sales@checkout-vault.com'
msg["To"] = "mconvert@ymail.com"

server = smtplib.SMTP(smtp_server, port)

try:
    # Установка соединения с SMTP сервером
    server.starttls()  # Используется для шифрования соединения
    server.login(username, password)
    server.sendmail(msg["From"], ["epishkin.serg@gmail.com"], msg.as_string())
    print("Email sent successfully")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()