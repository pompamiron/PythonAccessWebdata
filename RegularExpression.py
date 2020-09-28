# Chalakorn Manopirom // Use Regular Expression to find hindden number
# 


import re
fh = open('data1.txt')
sum = 0
lst = list()
for line in fh:
    x = re.findall('[0-9]+',line)
    if len(x) == 0:continue
    for count in x:
        number = int(count)
        lst.append(number)
        sum = sum + number
print(sum)
