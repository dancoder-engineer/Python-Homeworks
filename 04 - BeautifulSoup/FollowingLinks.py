from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error


def read_page(url, position):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    return tags[position-1].get('href', None)


url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
#url = "http://py4e-data.dr-chuck.net/known_by_Neeve.html"
position = 3
count = 4

for x in range(-1, count):
    print("Retrieving: " + url)
    url = read_page(url, position)

