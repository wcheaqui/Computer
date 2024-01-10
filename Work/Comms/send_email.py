from email.mime.text import MIMEText


def send_email(sender='', recipient='', subject='', message=''):
    """This function sends an email using the Mac OS built-in 'mail' library"""

    from email.mime.text import MIMEText

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Send the message from the Mac
    import smtplib
    s = smtplib.SMTP('0.0.0.0')
    # s.connect('willcheaqui@gmail.com')
    s.login('willcheaqui', 'Jamie23@marriage')
    s.send_message(msg)
    s.quit()


if __name__ == '__main__':
    send_email(sender='willcheaqui@gmail.com', recipient='willcheaqui@gmail.com', subject='test', message='this is a test')
    #
    import smtplib
    #
    # # server = smtplib.SMTP('localhost', 1025)
    #
    print(smtplib.SMTP())
    import socket

    print(socket.gethostbyname(""))

