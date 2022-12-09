import urllib.request, urllib.parse, urllib.error
import json

urlstem = "http://py4e-data.dr-chuck.net/json?"
#address = "South Federal University"
address = "Smolensk State University"

url = urlstem + urllib.parse.urlencode({'address': address, 'key': 42})
print("Retrieving " + url)

rawJson = urllib.request.urlopen(url).read().decode()
js = json.loads(rawJson)

print("Retrieved " + str(len(rawJson)) + " characters")
print("Place id " + js['results'][0]["place_id"])