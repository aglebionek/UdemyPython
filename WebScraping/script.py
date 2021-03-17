import requests
import bs4

website = requests.get("http://www.example.com")

soup = bs4.BeautifulSoup(website.text, "lxml")
print(soup.select('title')[0].getText())