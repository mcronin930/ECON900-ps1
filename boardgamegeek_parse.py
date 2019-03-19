from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()

one_file_name = "html_files/boardgame_2.html"

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
    print(game_rank)
    df = df.append({
        'rank': game_rank.strip()
        }, ignore_index=True)

print(games_rows)
df.to_csv("parsed_files/boardgame_dataset.csv")
# currencies_table = soup.find("table", {"id": "currencies"})
# currencies_tbody = currencies_table.find("tbody")
# currency_rows = currencies_tbody.find_all("tr")
