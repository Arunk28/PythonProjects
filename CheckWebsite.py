from MailLib import*

v =firstclass()

# v.sendmail("This is a test sending email through python","arun@syscloud.com,arunkumar280491@gmail.com","testmail").

content = v.isapprunning(config.URL_ADDR)
if not content:
    v.sendmail("Please check the app","arun@domain.com","AppDown")
else:
    if b'syscloud' in content:
        print(content)
    else:
        v.sendmail(config.URL_CHECK_BODY, config.TO_ADDR,config.URL_CHECK_SUBJECT)


o = fileoperation()
o.writefile()
