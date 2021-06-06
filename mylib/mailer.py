import smtplib, ssl

class Mailer:

    """
    This script initiaties the email alert function.

    """
    def __init__(self):
        
        self.EMAIL = "yousha.tsf@gmail.com"
        
        self.PASS = "*****"#password has been replaced here for privacy reasons
        self.PORT = 465
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)

    def send(self, mail):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)
        self.server.login(self.EMAIL, self.PASS)
        # message to be sent
        SUBJECT = 'ALERT! GO CHECK ENTRANCE'
        TEXT = f'People tailgating at your entrance!'
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        # sending the mail
        self.server.sendmail(self.EMAIL, mail, message)
        self.server.quit()
