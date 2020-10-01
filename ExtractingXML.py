# Chalakorn Manopirom
# Extracting Data from XML
# Data   : http://py4e-data.dr-chuck.net/comments_889070.xml
# Result : 2818


import urllib
import json
import xml.etree.ElementTree as ET

url=input("Input Url : ")
u=urllib.request.urlopen(url)
data=u.read()
xml_data=ET.fromstring(data)

search_str="comments/comment"
count_tags=xml_data.findall(search_str)

total=0
for tags in count_tags:
    c = tags.find('count')
    total = total + int(c.text)
    
print(total)
