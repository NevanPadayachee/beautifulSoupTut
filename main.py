import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://nevanpadayachee.herokuapp.com/")

soup = bs(r.content, features="html.parser")

#print(soup.prettify())

#first_header = soup.findAll("p")
#first_header = soup.find("p")
#first_header = soup.findAll(["p", "h1", "h2"])

#print(first_header)

#print(soup)
body = soup.find("body")
section = body.findAll("section", attrs={"id": "features"})
print(section)