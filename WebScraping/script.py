import requests
import bs4

#grabbing elements of a specific tag
website = requests.get("http://www.example.com") # request the html content
soup = bs4.BeautifulSoup(website.text, "lxml") # make it human redable
print(soup.select('title')[0].getText())

#grabbing elements with a specific class
res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(res.text,"lxml")
for item in soup.select('.toctext'): # select elements with class .toctext
    print(item.text)

#grabbing an image
res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, "lxml")
image = soup.select('img')[0]
image_link = requests.get(f"https:{image['src']}") # link to the first image that was found
f = open(f"image.jpg", 'wb') # save the image to a file called image.jpg
f.write(image_link.content)
f.close()

#GOAL: grab title of every book with 2 star rating
base_url = "http://books.toscrape.com/catalogue/page-{}.html"
#res = requests.get(base_url.format(1))
#soup = bs4.BeautifulSoup(res.text, "lxml")
#products = soup.select(".product_pod")
#example = products[0]
#print('star-rating Two' in str(example)) # dirty way
#print(example.select(".star-rating.Two")) # nicer way, replace spaces with dots
#example.select('a')[1]['title'] # the 2nd tag contains the title

#carefull, it takes for a while
two_star_titles = list()
for n in range(1, 51): # there are 50 pages with books
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")
    
    for book in books: # if the book has a different rating, the book.select list will be empty
        if book.select(".star-rating.Two"):
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)
            
