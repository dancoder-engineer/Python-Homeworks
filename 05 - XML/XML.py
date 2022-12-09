import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

mainCount = 0
count = 0

url = "http://py4e-data.dr-chuck.net/comments_42.xml"
#url2 = "http://py4e-data.dr-chuck.net/comments_1108918.xml"

#url = input("Enter location: ")
print("Retrieving " + url)

bytes = urllib.request.urlopen(url).read().decode()
xml = ET.fromstring(bytes)
xmlList=xml.findall('comments/comment/count')

for i in xmlList:
    mainCount += int(i.text)
    count += 1

print("Count: " + str(count))
print("Sum: " + str(mainCount))