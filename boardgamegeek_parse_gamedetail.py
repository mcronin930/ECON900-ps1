from bs4 import BeautifulSoup
import os
import glob
import pandas as pd
import re

if not os.path.exists("parsed_files_detail"):
	os.mkdir("parsed_files_detail")

df = pd.DataFrame()


for one_file_name in glob.glob("html_files_games/*.html"):

	print("parsing " + one_file_name)

	f = open(one_file_name, "r",  encoding="utf8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()

	#print(soup)

	game = soup.find("div", {"id": "mainbody"}).find("div", {"class": "panel panel-condensed"})
	game_stats = game.find_all("div", {"class":"outline-item-description"})

	game_weight = " ".join(game_stats[3].text.split())
	game_fans = game_stats[5].text.strip()
	game_cat = " ".join(soup.find_all("div", {"class": "game-header-ranks hidden-game-header-collapsed"})[0].text.split())
	game_players = " ".join(soup.find("div", {"class": "game-header game-header-collapsed"}).find("div", {"class": "panel-body"}).find_all("div", {"class": "gameplay-item-primary"})[0].text.split())
	game_time = " ".join(soup.find("div", {"class": "game-header game-header-collapsed"}).find("div", {"class": "panel-body"}).find_all("div", {"class": "gameplay-item-primary"})[1].text.split())
	game_age = " ".join(soup.find("div", {"class": "game-header game-header-collapsed"}).find("div", {"class": "panel-body"}).find_all("div", {"class": "gameplay-item-primary"})[2].text.split())

	print(game_weight)
	print(game_fans)
	print(game_cat)
	print(game_players)
	print(game_time)
	print(game_age)
