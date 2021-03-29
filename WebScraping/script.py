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