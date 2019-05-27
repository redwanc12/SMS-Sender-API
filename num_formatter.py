"""To find a specific carrier extension for a number"""

PROVIDERS = {
    'ATT':'@txt.att.net',
    'TMOBILE':'@tmomail.net ',
    'Verizon':'@vtext.com',
    'Sprint':'@messaging.sprintpcs.com',
    'XFinity':'@vtext.com',
    'Virgin':'vmobl.com',
    'Cricket':'sms.cricketwireless.net'
}


class Formatter:
    """Class to format a number into email form"""

    @staticmethod
    def format_num(num, carrier):
        """formats a phone number to email format"""
        if '+1' not in num:
            num = '+1' + num
        extension = PROVIDERS[carrier]
        return num+extension
