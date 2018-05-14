# load the url
# from urllib.request import urlopen
# html = urlopen("http://www.google.com/").read()
# print(html)

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




# comment the code
# a, b, c = 1, 2, "john"
# print (c)
# k = True
# k= False
# if k:
#     print (k)
# print("arun")