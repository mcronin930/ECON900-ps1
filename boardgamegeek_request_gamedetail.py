import os
import random
from bs4 import BeautifulSoup
import glob
import pandas as pd
import time
import numpy as np
from selenium import webdriver


## Creates a directory of html files
if not os.path.exists("html_files_games"):
	os.mkdir("html_files_games")

df = pd.read_csv("parsed_files/boardgame_dataset.csv")
game_list = df[np.isfinite(df['rank'])]


ext = game_list.sort_values('rank').link

i = 1
for e in ext:
	print(i)
	url = "https://boardgamegeek.com" + e + "/stats"
	print(url)

	name =e.replace("/", "_")

	file_name = "html_files_games/{}.html".format(name)
	print(file_name)
	html_file = open(file_name, "w", encoding="utf8")
	browser = webdriver.Firefox()
	browser.get(url)
	response = browser.page_source

	html_file.write(response)
	html_file.close

	browser.close()

	i = i+1

	t = 3 + random.randint(-2, 2)
	time.sleep(t)
