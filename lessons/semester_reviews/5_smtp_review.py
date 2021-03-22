import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP is an abbreviation for Simple Mail Transfer Protocol, which is used to communicate with mail
# servers. SMTP is specifically a *delivery* protocol in that you can only send mail using it, but
# you cannot retrieve mail. Python comes with the smtplib module, which handles all of the different
# parts of the SMTP protocol.

def texter(timestamp):
    email = "firstlast.pi@gmail.com" 
    password = "fakepassword123!" # Don't forget to remove sensitive information before pushing to
                                  # a repository.

    sms_gateway = "PHONE_NUMBER@CARRIER_GATEWAY" # Short Message Service (SMS) gateway is a
                                                 # mechanism by which SMS messages are sent and
                                                 # received.

    smtp = "smtp.gmail.com"
    port = 587 # A port is a communication endpoint in computer networking.

  
    server = smtplib.SMTP(smtp, port) # This starts the email server using Google's server and the
                                      # specified port number.

    server.starttls() # STARTTLS is a way to take an existing insecure connection and upgrade it to
                      # a secure connection using SSL/TLS. Secure Sockets Layer (SSL) and Transport
                      # Layer Security (TLS) protocols designed to provide communications security
                      # over a computer network.

    server.login(email, password)

    msg = MIMEMultipart() # Multipurpose Internet Mail Extensions (MIME) is an Internet standard
                          # that is used to support the transfer of single or multiple text and
                          # non-text attachments. If a message in MIME format contains multiple
                          # related parts, the Content-Type parameter is set to Multipart.
    msg['From'] = email
    msg['To'] = sms_gateway

    msg['Subject'] = "FamCam Alert!\n" # "\n" is used to indicate a new line should be used for the
                                       # next output.
    body = f"Motion has been detected at {timestamp}!\n"

    msg.attach(MIMEText(body, 'plain')) # The MIMEText class is used to create MIME objects.
                                        # "msg.attach()" attaches the instantiated MIMEText object
                                        # to the MIMEMultipart object.

    sms = msg.as_string() # This returns the entire formatted message as a string.

    server.sendmail(email, sms_gateway, sms) # This sends the message over an open connection.

    server.quit() # This closes the connection to the email server.