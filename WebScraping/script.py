import requests
import bs4

website = requests.get("http://www.example.com")

soup = bs4.BeautifulSoup(website.text, "lxml")
print(soup.select('title')[0].getText())

res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(res.text,"lxml")
for item in soup.select('.toctext'): # select elements with class .toctext
    print(item.text)
