import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.request import urlopen
import ssl



class firstclass:
    def __init__(self):
        self.name = "Arun Kumar"
    def printname(self):
        return self.name
    def sendmail(self,message,to,subject):
        # http://www.pythonforbeginners.com/code-snippets-source-code/using-python-to-send-email
        # http://naelshiab.com/tutorial-send-email-python/
        msg = MIMEMultipart()
        msg['From'] = "arunk@syscloudtech.in"
        msg['To'] = to
        msg['Subject'] = subject
        fromaddr = "arunk@syscloudtech.in"
        toaddr = to

        body = message  # redundant parentheses
        msg.attach(MIMEText(body, 'plain'))  # redundant parentheses

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(config.FROM_ADDR, config.FROM_PWD)
        text = msg.as_string()
        server.sendmail(fromaddr,toaddr,text)
        server.quit()

    def isapprunning(self,url):
        context = ssl._create_unverified_context()
        html = urlopen(url,context=context).read()
        return html;

class config:
    TO_ADDR ="arun@syscloud.com"
    URL_ADDR ="https://app.syscloud.com/"
    FROM_ADDR ="arunk@syscloudtech.in"
    FROM_PWD ="xxxxxxxxxxxxxx"
    URL_CHECK_BODY="Please check the app.syscloud.com"
    URL_CHECK_SUBJECT = "AppDown"

# File operation
class fileoperation:
    def writefile(self):
        file1 = open(r"D:\MyFile2.txt","a")
        file1.write("test write python")
        file1.close()





