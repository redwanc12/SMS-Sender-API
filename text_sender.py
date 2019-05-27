"""Class to send a text message once all information is already found"""
import smtplib

class Client:
    """Class to handle the client"""
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_message(self, toNumber, carrierExt, message):
        """Sends a SMS message to a number using its carrier extension"""
        host = smtplib.SMTP( "smtp.gmail.com", 587)
        host.starttls()
        host.login(self.email, self.password)
        host.sendmail(
            self.email,
            f'{toNumber}{carrierExt}',
            message
        )
