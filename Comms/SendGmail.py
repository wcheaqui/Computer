

# Define the email function (dont call it email!)
def send_emails(email_to: list, email_from: str, password: str, body: str, subject: str = 'No Subject',
                attachment_filename: str = ''):

    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    # Setup port number and server name

    smtp_port = 587  # Standard secure SMTP port
    smtp_server = "smtp.gmail.com"  # Google SMTP Server

    # Connect with the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email_from, password)
    print("Successfully connected to server")
    print()

    for person in email_to:

        # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject
        msg['Body'] = body

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))

        if attachment_filename != '':

            # Open the file in python as a binary
            attachment = open(attachment_filename, 'rb')  # r for read and b for binary

            # Encode as base 64
            attachment_package = MIMEBase('application', 'octet-stream')
            attachment_package.set_payload(attachment.read())
            encoders.encode_base64(attachment_package)
            attachment_package.add_header('Content-Disposition', "attachment; filename= " + attachment_filename)
            msg.attach(attachment_package)

        # Cast as string
        text = msg.as_string()

        # Send emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    # Close the port
    TIE_server.quit()










