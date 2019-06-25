import requests as rq
from bs4 import BeautifulSoup

response=rq.get("https://en.wikipedia.org/wiki/Google")
out=BeautifulSoup(response.content,"html.parser")
print(out.text)
f=open("input.txt", "w+",encoding="utf-8")
f.write(out.text)
f.close()