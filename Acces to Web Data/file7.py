# Twitter API
import urllib.request, urllib.parse, urllib.error
from twurl import augment
import oauth
import ssl

print("Asking for twitt")
url = augment('http://api.twitter')
