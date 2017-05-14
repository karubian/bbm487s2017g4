import smtplib


class MailClient:
    def __init__(self) -> None:
        super().__init__()

    def send_email(self,name_to,email_to,book_name):

        gmail_user = 'buraktest9@gmail.com'
        gmail_password = 'testburak9'

        sent_from = gmail_user
        to = [email_to]
        email_text = "Hey "+ name_to +"!" + "\n\nThe book called \""+ book_name + "\" is available now to rent.Hurry up!"
        subject = "Library Notification"
        message = 'Subject: {}\n\n{}'.format(subject, email_text)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, message)
            server.close()

            print('Email sent!')
        except:
            print('Something went wrong...')

