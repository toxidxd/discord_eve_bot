import requests, bs4, random, time, csv, re

print ('eve_killboard_parser_by_toxidxd')
#corp link https://zkillboard.com/corporation/98636833/
#char link https://zkillboard.com/character/2117056606/
last_id = 0
link = "https://zkillboard.com"
soup = requests.get(link) #запрашиваем страницу
soup = bs4.BeautifulSoup(soup.text, "html.parser") #скармливаем её парсеру
killid = soup.find_all('tr', {"class": "killListRow"}) #находим все теги tr с заданным классом
last_id = killid[0]['killid']
print ("last id at start: ", last_id)
print ('---------------------------------------')

while True:
    soup = requests.get(link) #запрашиваем страницу
    soup = bs4.BeautifulSoup(soup.text, "html.parser") #скармливаем её парсеру
    print ('---------------------------------------')
    killid = soup.find_all('tr', {"class": "killListRow"}) #находим все теги tr с заданным классом

    if killid[0]['killid'] == last_id:
        print ("no new kills", killid[0]['killid'])
        ('---------------------------------------')
    else:
        for kill in killid:
            if kill['killid'] == last_id:
                print ("all printed")
                break
            else:
                print(kill['killid'])
        ('---------------------------------------')
        last_id = killid[0]['killid']
        print ("new last id", last_id)



    sl = random.randint(23,32)
    print("Sleep ", sl, " sec")
    time.sleep(sl)
