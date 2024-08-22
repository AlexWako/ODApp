import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Send an email for exchange

def exchange(email, body):

    server = 
    port =
    send_email = 
    send_password = 
    rec_email = email
    subject = "Message from Okayama Denim"
    body = MIMEText(body, 'html')

    print(body)

    message = MIMEMultipart()
    message['From'] = send_email
    message['To'] = rec_email
    message['Subject'] = subject

    # Add body to the email
    message.attach(body)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(server, port) as server:
        server.starttls()
        server.login(send_email, send_password)
        server.send_message(message)
        server.quit()
