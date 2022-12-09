from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

count = 0
sum = 0

url = "http://py4e-data.dr-chuck.net/comments_1108916.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags=soup('span')
for tag in tags:
    count += 1
    sum += int(tag.contents[0])

print("Count " + str(count))
print("Sum " + str(sum))