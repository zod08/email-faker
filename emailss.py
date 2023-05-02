import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def envoyer_mail(sender_email, email_destinataire,sujet, message):
    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = sujet
    multipart_message["From"] = sender_email
    multipart_message["to"] = email_destinataire

    multipart_message.attach(MIMEText(message, "plain"))


    server_mail = smtplib.SMTP("smtp-relay.sendinblue.com", 587)
    server_mail.starttls()
    server_mail.login("newtrade690@gmail.com", "RXtPScQh9IAqMabU")
    server_mail.sendmail(sender_email, email_destinataire, multipart_message.as_string())
    server_mail.quit()



#envoyer_mail(sender_email, email_destinataire , Objet_mail, message_mail)
