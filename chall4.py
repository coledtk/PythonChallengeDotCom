import requests
import re
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
response = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345", verify=False)
x = "".join(re.findall("[0-9][0-9][0-9][0-9][0-9]",response.text))
y = url + x
print(y)
while True:
    response = requests.get(y, verify=False)
    x = "".join(re.findall("[0-9]{3,5}$",response.text))
    y = url + x
    print(y)
    if x == '16044':
        y = url + '8022'
    else:
        continue
#peak.html is shown when the last request returns nothing.
        
