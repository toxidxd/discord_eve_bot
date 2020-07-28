import requests, bs4, random, time, csv

print ('hell')
#corp link https://zkillboard.com/corporation/98636833/
link = "https://zkillboard.com/character/2117056606/"
soup = requests.get(link)
soup = bs4.BeautifulSoup(soup.text, "html.parser")
print (soup)
