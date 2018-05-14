
# load the url content
# https://stackoverflow.com/questions/17178483/how-do-you-send-an-http-get-web-request-in-python
from urllib.request import urlopen
html = urlopen("http://www.google.com/").read()
print(html)