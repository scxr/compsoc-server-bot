import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://devpost.com/hackathons?order_by=deadline&status[]=upcoming')
soup = BeautifulSoup(driver.page_source)
driver.close()
hackathons = soup.find_all("div", {"class":"main-content"})
hackathon_list = []
for hackathon in hackathons:
    thumbnail = hackathon.find_all("img",{"class":"hackathon-thumbnail"})[0]
    actual_thumbnail = "https:" + str(thumbnail["src"])
    title = hackathon.find_all("h3", {"class":"mb-4"})[0].text
    sub_date = hackathon.find_all("div", {"class":"submission-period"})[0].text
    prizes = hackathon.find_all("span", {"class":"prize-amount"})[0].text
    hackathon_url = hackathon.find_all("a")
    print(hackathon_url) 
    hackathon_scraped = (actual_thumbnail, title, sub_date, prizes)
    hackathon_list.append(hackathon_scraped)
