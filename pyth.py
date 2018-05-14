
# ref https://www.journaldev.com/19213/python-http-client-request-get-post
# http://www.pythonforbeginners.com/loops/for-while-and-nested-loops-in-python
# http://developer.rhino3d.com/guides/rhinopython/python-xml-json/
import http.client
import json
conn = http.client.HTTPConnection("jsonplaceholder.typicode.com")
headers = {'Content-type': 'application/json'}
conn.request("GET", "/users", "", headers)

res = conn.getresponse()
h= res.read().decode()
j=json.loads(h)
for m in j:
    print(m["name"])



# load the url content
from urllib.request import urlopen
html = urlopen("http://www.google.com/").read()
print(html)


# basic variable declaration
a, b, c = 1, 2, "john"
print (c)
k = True
k= False
if k:
    print (k)
print("arun")