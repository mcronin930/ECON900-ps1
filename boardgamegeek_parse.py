from bs4 import BeautifulSoup
import os
import glob
import pandas as pd
import re

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()


for one_file_name in glob.glob("html_files/*.html"):

	print("parsing " + one_file_name)

	f = open(one_file_name, "r",  encoding="utf8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()

	games_table = soup.find("table", {"id": "collectionitems"})
	games_tbody = games_table.find("tbody")
	games_rows = games_table.find_all("tr")
	games_rows.pop(0)
	#
	for r in games_rows:

		game_rank = r.find("td", {"class": "collection_rank"}).text
		game_link = r.find("td", {"class": "collection_objectname"}).find("a",href = True).get('href')
		game_name = r.find("td", {"class": "collection_objectname"}).find("a",href = True).text

		if r.find("td", {"class": "collection_objectname"}).find("span") == None:
			game_year = ""
		else:
			game_year = r.find("td", {"class": "collection_objectname"}).find("span").text

		game_geek_r = r.find_all("td", {"class": "collection_bggrating"})[0].text
		game_avg_r = r.find_all("td", {"class": "collection_bggrating"})[1].text
		game_vote_count = r.find_all("td", {"class": "collection_bggrating"})[2].text
		game_p = " ".join(r.find("td", {"class": "collection_shop"}).text.split())

		df = df.append({
		    'file_name': one_file_name,
		    'rank': game_rank.strip(),
		    'link': game_link.strip(),
		    'name': game_name.strip(),
		    'year': game_year.strip().replace("(", "").replace(")", ""),
		    'geek_rating': game_geek_r.strip(),
		    'avg_rating': game_avg_r.strip(),
		    'vote_count': game_vote_count.strip(),
		    'price': game_p
		    }, ignore_index=True)

		df.to_csv("parsed_files/boardgame_dataset.csv")
