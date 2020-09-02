import requests, bs4, random, time, csv, re, selenium
from selenium import webdriver

chromedriver = './chromedriver'
options = webdriver.ChromeOptions()
#options.add_argument('headless')
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

def page_request (link):

    print('get link')
    browser.get(link)
    print('wait 10 sec')
    time.sleep(10)
    requiredHtml = browser.page_source
    return requiredHtml

def page_refresh():
    browser.refresh
    time.sleep(5)


print ('eve_killboard_parser_by_toxidxd')
#corp link https://zkillboard.com/corporation/98636833/
#char link https://zkillboard.com/character/2117056606/
last_id = 0
link = "https://zkillboard.com"

soup = page_request(link) #запрашиваем страницу
soup = bs4.BeautifulSoup(soup, "html.parser") #скармливаем её парсеру
killid = soup.find_all('tr', {"class": "killListRow"}) #находим все теги tr с заданным классом
last_id = killid[0]['killid']
print ("last id at start: ", last_id)
print ('---------------------------------------')

while True:
    #soup = page_request(link) #запрашиваем страницу
    page_refresh()
    requiredHtml = browser.page_source
    soup = bs4.BeautifulSoup(requiredHtml, "html.parser") #скармливаем её парсеру
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



    #sl = random.randint(23,32)
    #print("Sleep ", sl, " sec")
    #time.sleep(sl)
    print("end of while")
