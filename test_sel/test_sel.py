import selenium, requests, bs4, random, time, csv, re
from selenium import webdriver


link = "https://zkillboard.com/corporation/98636833/"
chromedriver = './chromedriver'
options = webdriver.ChromeOptions()
#options.add_argument('headless')  # для открытия headless-браузера
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

browser.get(link)
time.sleep(15)
requiredHtml = browser.page_source
print(requiredHtml)
k_soup = bs4.BeautifulSoup(requiredHtml.text, "html.parser")

print(k_soup)
