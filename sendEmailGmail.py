import smtplib, ssl 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

TO = 'jeff@jeffl.xyz'
SUBJECT = 'email subject line'
TEXT = '<html><p>here is my email</p></html>'
html = MIMEText(TEXT, "html")

gmail_sender = 'jeffrey.leibensperger@gmail.com'
gmail_passwd = 'MYGMAILPASSWORD'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    println('email sent successfully')
except:
    print ('error sending email')

server.quit()
