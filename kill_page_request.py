import requests, bs4, random, time, csv, re

def kill_parser(lnk):
    print (lnk)
    k_soup = requests.get(lnk)
    k_soup = bs4.BeautifulSoup(k_soup.text, "html.parser")
    vic_name = k_soup.find_all('table', {"class": "table table-condensed"})
    print (vic_name[0].find_all('a'))
    print("-----------------------------------------")
    print (vic_name[0])
    print("-----------------------------------------")
    print (vic_name[0]['style'])
    print("-----------------------------------------")

    print (type(vic_name))
    print (type(vic_name[0]))





print ("kill_data_parser")
link = "https://zkillboard.com/kill/86211274/"
kill_parser(link)
