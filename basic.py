from fc import*

# basic variable declaration
# a, b, c = 1, 2, "john"
# print (c)
# k = True
# k= False
# if k:
#     print (k)
# print("arun")
#
# paragraph = """This is a paragraph. It is
# made up of multiple lines and sentences."""
# print(paragraph)
# input("\n\nPress the enter key to exit.")

v =firstclass()
print(v.printname())

# v.sendmail("This is a test sending email through python","arun@syscloud.com,arunkumar280491@gmail.com","testmail").

content = v.isapprunning("https://Google.com/")
if not content:
    v.sendmail("Please check the app.syscloud.com","arun@syscloud.com","AppDown")
else:
    if b'syscloud' in content:
        print(content)
    else:
        v.sendmail("Please check the app.syscloud.com", "arun@syscloud.com", "AppDown")


