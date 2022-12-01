import urllib.request, urllib.parse, urllib.error
import json

count = 0
sum = 0

url = "http://py4e-data.dr-chuck.net/comments_42.json"
#url = "http://py4e-data.dr-chuck.net/comments_1108919.json"

#url = input("Enter location: ")

print("Retrieving " + url)

js = urllib.request.urlopen(url).read().decode()
dict = json.loads(js)

jsLen = len(js)

print("Retrieved " +str(jsLen) + " characters")

for i in dict["comments"]:
    count += 1
    sum += i["count"]

print("Count: "+str(count))
print("Sum: "+str(sum))
