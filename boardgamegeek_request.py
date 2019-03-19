import urllib.request
import os
from random import *
from bs4 import BeautifulSoup
import glob
import pandas as pd
import random
import time
from selenium import webdriver


## Creates a directory of html files
if not os.path.exists("html_files"):
	os.mkdir("html_files")


i = 1
while i > 0:
    print(i)
    file_name = "html_files/boardgame_{}.html".format(i)
    print(file_name)
    html_file = open(file_name, "w", encoding="utf8")

    # Java is used to populate price data on the webpage
    # The selenium webdriver is needed to trigger the java
    url = "https://boardgamegeek.com/browse/boardgame/page/{}".format(i)
    print(url)
    browser = webdriver.Firefox()
    browser.get(url)
    response = browser.page_source

    html_file.write(response)
    html_file.close

    browser.close()

    # The html needs to be parsed to see if table on the given page is populated
    # if the table is not populated the program will stop running (end of list of games has been reached)
    f = open(file_name, "r", encoding="utf8")
    soup = BeautifulSoup(f.read(), 'html.parser')
    f.close()
    table = soup.find("table", {"id": "collectionitems"})
    empty = table.find_all("td")
    if empty == []:
         i = 0
    else:
         i = i+1
    print(i)

    # The random number generator initiates random sleep times for the loop
    t = 10 + random.randint(-5, 5)
    time.sleep(t)
