# load the url
from urllib.request import urlopen
html = urlopen("http://www.google.com/").read()
print(html)

# comment the code
# a, b, c = 1, 2, "john"
# print (c)
# k = True
# k= False
# if k:
#     print (k)
# print("arun")