import requests
import bs4

session = requests.Session()
website = session.get(url="http://auctions.craftlink.xyz/", allow_redirects=True)
cookies = dict(website.cookies)
website = session.get(url="http://auctions.craftlink.xyz/", allow_redirects=True, cookies=cookies, verify=False)

#soup = bs4.BeautifulSoup(website.text, "lxml")
print(website.status_code, website.__dict__.get('location'))
#print(soup)
#newest_auctions = soup.find_all('div', attrs={'class': 'bg-gray-900 p-3 rounded-lg shadow-lg'})
#print(newest_auctions[0].gettext())