#Chalakorn Manopirom  

# Scraping Numbers from HTML using BeautifulSoup


import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

con =ssl.create_default_context()
con.check_hostname=False
con.verify_mode=ssl.CERT_NONE

link= "http://py4e-data.dr-chuck.net/comments_523067.html"
html=urllib.request.urlopen(link,context=con).read()
soup=BeautifulSoup(html,'html.parser')

tags=soup('span')
sum =0
count =0

for tag in tags:
    count = count+1
    sum = sum + int(tag.contents[0])
print ("Count : ", count)
print ("Sum : ",sum)
