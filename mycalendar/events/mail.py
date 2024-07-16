import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email_gmail(subject, body, to_email, from_email, password):
    # Настраиваем соединение с сервером SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    try:
        # Логинимся на сервере
        server.login(from_email, password)

        # Создаем сообщение
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Отправляем письмо
        server.sendmail(from_email, to_email, msg.as_string())
        print("Email sent successfully.")

    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()


SUBJECT = "Test Subject"
BODY = "This is a test email sent from Python."
TO_EMAIL = "mr.dan.efremov@yandex.ru"
FROM_EMAIL = "clopov.egor2016@gmail.com"
PASSWORD = "awvn zmtt hslk dvsq"
