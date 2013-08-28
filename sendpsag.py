import time
import datetime
import commands
import re
import smtplib

####--[CONFIGURATION]
server = 'smtp.gmail.com' #smtp server address
server_port = '587' #port for smtp erver

username = 'myemail@gmail.com' #gmail account
password = 'password' #password for that gmail account

fromaddr = 'myemail@gmail.com' #address to send from
toaddr = '1234567890@mms.att.net' #address to send IP to
####--[/CONFIGURATION]

now = datetime.datetime.now()
message = 'Raspberry Pi: Power sag occured on ' + now.isoformat()

headers = ["From: " + fromaddr,
           "To: " + toaddr,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)

server = smtplib.SMTP(server + ':' + server_port)  
server.ehlo()
server.starttls()  
server.ehlo()
server.login(username,password)  
server.sendmail(fromaddr, toaddr, headers + "\r\n\r\n" +  message)  
server.quit()
