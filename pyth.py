# load the url
# from urllib.request import urlopen
# html = urlopen("http://www.google.com/").read()
# print(html)

import http.client
conn = http.client.HTTPConnection("api.github.com")
headers = {"Content-type":"application/json","UserAgent ":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
conn.request("GET", "/meta", "", headers)

res = conn.getresponse()
print(res.status)




# comment the code
# a, b, c = 1, 2, "john"
# print (c)
# k = True
# k= False
# if k:
#     print (k)
# print("arun")