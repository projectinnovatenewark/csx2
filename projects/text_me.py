import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def texter(timestamp):
  email = "your.email.here@gmail.com" # This should be deleted in between uses so sensitive information is not pushed to your remote repository
  password = "INSERT PASSWORD FOR ABOVE EMAIL" # This should be deleted in between uses so sensitive information is not pushed to your remote repository

  sms_gateway = "PHONE_NUMBER@CARRIER_GATEWAY" # This should be deleted in between uses so sensitive information is not pushed to your remote repository

  smtp = "smtp.gmail.com"
  port = 587

  # This starts the email server
  server = smtplib.SMTP(smtp,port)

  server.starttls()

  server.login(email,password)

  msg = MIMEMultipart()
  msg['From'] = email
  msg['To'] = sms_gateway

  msg['Subject'] = "FamCam Alert!\n" # "/n" is used to indicate a new line should be used for the next output
  body = f"Motion has been detected at {timestamp}!\n"

  msg.attach(MIMEText(body, 'plain'))

  sms = msg.as_string()

  server.sendmail(email,sms_gateway,sms)

  server.quit()