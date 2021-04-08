#%%
#TASK: Import any libraries you think you'll need to scrape a website.
import requests
import bs4

#TASK: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.
res = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text, "lxml")

#TASK: Get the names of all the authors on the first page.
authors_set = set()
for author in soup.select(".author"):
    authors_set.add(author.text)

#TASK: Create a list of all the quotes on the first page.
quotes_list = list()
for quote in soup.select(".text"):
    quotes_list.append(quote.text)

#TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right
#from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath each quote,
#try to find a class only present in the top right tags, perhaps check the span.
tags_list = list()
for tag in soup.select(".tag-item"):
    tags_list.append(tag.text.strip())

#TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/.
#Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors
#on the website. Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out
#how to check that your loop is on the last page with quotes. For debugging purposes, I will let you know that there are
#only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough
#that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!
url = 'http://quotes.toscrape.com/page/{}/'
authors_set2 = set()
for i in range(1, 101):
    try: res = requests.get(url.format(i))
    except: break

    soup = bs4.BeautifulSoup(res.text, "lxml")

    quotes = soup.select(".text")
    if not quotes: break

    for author in soup.select(".author"):
        authors_set2.add(author.text)
# %%
