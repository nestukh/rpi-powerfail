import time
import datetime
import commands
import re
import smtplib
#import urllib2

####--[COFIGURATION]
server = 'smtp.gmail.com' #smtp server address
server_port = '587' #port for smtp erver

username = 'myemail@gmail.com' #gmail account
password = 'password' #password for that gmail account

fromaddr = 'myemail@gmail.com' #address to send from
toaddr = '1234567890@mms.att.net' #address to send IP to
now = datetime.datetime.now()
message = 'Raspberry Pi: Power failure occured on ' + now.isoformat()
####--[/COFIGURATION]

#the interface may be wifi and it needs time to initialize
#so wait a little bit before parsing ifconifg
#time.sleep(30)

#extract the ip address (or addresses) from the ifconfig
#found_ips = []
#ips = re.findall( r'[0-9]+(?:\.[0-9]+){3}', commands.getoutput("/sbin/ifconfig"))
#ext_ip=urllib2.urlopen('http://ip.42.pl/raw').read()
#for ip in ips:
#	if ip.startswith("255") or ip.startswith("127") or ip.endswith("255"):
#		continue
#	found_ips.append(ip)

#found_ips.append(ext_ip)
#message += ", ".join(found_ips)
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
