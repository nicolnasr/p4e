import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1052882.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0

tags = soup('span')
for tag in tags:
    tagtxt = tag.text
    sum = sum + int(tagtxt)

print(sum)