# Chalakorn Manopirom

# The program will use urllib to read the HTML from the data files below, 
# extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, 
# follow that link and repeat the process a number of times and report the last name you find.

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import urllib

con=ssl.create_default_context()
con.check_hostname=False
con.verify_mode=ssl.CERT_NONE

link=input("Enter URL:")
count=int(input("Enter count:"))
pos=int(input("Enter position:"))

print ("Retriving: ",link)
for i in range(0,count):
    html=urllib.request.urlopen(link).read()
    soup=BeautifulSoup(html)
    tags=soup('a')
    
    link=tags[pos-1].get('href')

result=tags[pos-1].contents[0]
print (result)
