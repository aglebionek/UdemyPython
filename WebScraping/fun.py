import requests
import bs4

website = requests.get(url="https://auctions.craftlink.xyz/", allow_redirects=True)

soup = bs4.BeautifulSoup(website.text, "lxml")
print(soup)
newest_auctions = soup.find_all('div', attrs={'class': 'bg-gray-900 p-3 rounded-lg shadow-lg'})
print(newest_auctions[0].gettext())