import urllib.request
import os
from random import *
from bs4 import BeautifulSoup
import glob
import pandas as pd
import random
import time


## Creates a directory of html files
if not os.path.exists("html_files"):
	os.mkdir("html_files")

i = i
while i > 0:
     print(i)
     file_name = "html_files/boardgame_{}.html".format(i)
     print(file_name)
     f = open(file_name, "wb")
     url = "https://boardgamegeek.com/browse/boardgame/page/{}".format(i)
     print(url)
     response = urllib.request.urlopen(url)
     html = response.read()
     f.write(html)
     f.close()

     # The purpose of parsing the html here is to see if the table on the page is empty
     # if the table is empty, then all the board game data has been scraped and the program will stop requesting
     f = open(file_name, "r",  encoding="utf8")
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
