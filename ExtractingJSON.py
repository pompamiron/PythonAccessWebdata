# Chalakorn Manopirom
# Extracting Data from JSON
# Data : http://py4e-data.dr-chuck.net/comments_889071.json
# Result : 2640

import urllib
import json

url=input("Input Url :")
u=urllib.request.urlopen(url)
dat=u.read()
data=json.loads(dat)

total=0

for tags in data["comments"]:
    total = total + tags["count"]
print(total)
