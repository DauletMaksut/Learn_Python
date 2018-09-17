#Parsing web
#Soup works for xml and html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

cfx = ssl.create_default_context()
cfx.check_hostname = False
cfx.verify_mode = ssl.CERT_NONE

url = input('Enter ')
html = urllib.request.urlopen(url,context = cfx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup ('a')
for tag in tags:
    print(tag.get('href', None))
